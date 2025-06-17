import os
import pandas as pd

def load_csv(file_path='../Data/data.csv'):
    """
    Loads data from a CSV file.
    If the file is not found, a dummy DataFrame is created for demonstration purposes.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Creating a dummy DataFrame for demonstration.")

def export_dataframe_to_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Exports a Pandas DataFrame to a CSV file in the 'data' folder in the parent directory.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        filename (str): The name of the CSV file to create (e.g., 'exported_data.csv').
    """
    # Get the parent directory of the current script
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(parent_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, filename)
    try:
        df.to_csv(file_path, index=False)
        print(f"\nDataFrame successfully exported to '{file_path}'!")
    except Exception as e:
        print(f"Error exporting DataFrame to CSV: {e}")
