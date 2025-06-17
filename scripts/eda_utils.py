# scripts/eda_utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display


def describe_numerics(df, columns):
    print("\nDescriptive Statistics:\n")
    display(df[columns].describe().T)


def plot_boxplots(df, columns):
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()


def plot_distributions(df, columns):
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, bins=50)
        plt.title(f'Distribution of {col}')
        plt.show()


def plot_correlation_matrix(df, columns):
    plt.figure(figsize=(8, 6))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()


def plot_time_series(df, time_col, value_cols):
    plt.figure(figsize=(12, 6))
    for col in value_cols:
        sns.lineplot(data=df, x=time_col, y=col, label=col)
    plt.xticks(rotation=45)
    plt.title('Trends Over Time')
    plt.legend()
    plt.tight_layout()
    plt.show()


def analyze_vehicle_claims(df):
    top = df.groupby(['make', 'Model'])['TotalClaims'].mean().sort_values(ascending=False).head(10)
    low = df.groupby(['make', 'Model'])['TotalClaims'].mean().sort_values().head(10)
    return top, low


def plot_avg_loss_by_category(df, category_col):
    plt.figure(figsize=(10, 5))
    avg_loss = df.groupby(category_col)['LossRatio'].mean().sort_values()
    sns.barplot(x=avg_loss.index, y=avg_loss.values)
    plt.title(f'Average Loss Ratio by {category_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_heatmap(df, row_cat, col_cat, value_col):
    heatmap_data = df.groupby([row_cat, col_cat])[value_col].mean().unstack()
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title(f'Heatmap of {value_col} by {row_cat} and {col_cat}')
    plt.show()
