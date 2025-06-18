import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

def calculate_claim_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['MadeClaim'] = df['TotalClaims'] > 0
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    return df

def perform_ttest(group_a, group_b, metric: str):
    return ttest_ind(group_a[metric], group_b[metric], equal_var=False)

def perform_chi_squared(contingency_table):
    chi2, p, _, _ = chi2_contingency(contingency_table)
    return chi2, p

def test_difference_between_groups(df, group_col, metric_col, group_val_a, group_val_b):
    group_a = df[df[group_col] == group_val_a]
    group_b = df[df[group_col] == group_val_b]
    stat, p = perform_ttest(group_a, group_b, metric_col)
    return {
        "group_a": group_val_a,
        "group_b": group_val_b,
        "metric": metric_col,
        "t_stat": stat,
        "p_value": p,
        "significant": p < 0.05
    }
