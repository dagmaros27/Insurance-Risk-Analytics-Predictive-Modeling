import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error, r2_score
import shap
import matplotlib.pyplot as plt

def prepare_data(df):
    df = df.copy()

    # Focus on records with actual claims
    df = df[df['TotalClaims'] > 0]
    print("Rows after filtering TotalClaims > 0:", len(df))

    # Ensure TotalClaims is numeric
    df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')

    # Drop irrelevant or high-cardinality columns
    drop_cols = [
        'UnderwrittenCoverID', 'PolicyID', 'TransactionMonth', 'VehicleIntroDate',
        'make', 'Model', 'Section', 'Product'
    ]
    df.drop(columns=[col for col in drop_cols if col in df.columns], inplace=True)

    # Handle missing values BEFORE encoding
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype == 'bool':
            df[col].fillna('Unknown', inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)

    # One-hot encode categorical columns
    cat_cols = df.select_dtypes(include=['object', 'bool']).columns
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    print("Rows after preprocessing:", len(df))
    return df



def train_model(df):
    X = df.drop(columns=['TotalClaims'])
    y = df['TotalClaims']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    return model, X_train, X_test, y_test, preds, rmse, r2

def interpret_model(model, X_train):
    # Ensure data is numeric
    if isinstance(X_train, pd.DataFrame):
        if X_train.select_dtypes(include=['object']).shape[1] > 0:
            raise ValueError("X_train contains non-numeric (object) columns. Please one-hot encode or convert them.")
    
    # TreeExplainer for tree-based models like RandomForest
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)

    # Bar summary of feature importances
    shap.summary_plot(shap_values, X_train, plot_type="bar", show=False)
    plt.title("Top Features by SHAP Values")
    plt.tight_layout()
    plt.show()

    # Detailed plot for top row
    shap.initjs()
    shap.force_plot(explainer.expected_value, shap_values[0], X_train.iloc[0], matplotlib=True)
