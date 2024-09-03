import pandas as pd
import os

def load_data(file_path=None):
    """
    Load the data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file. If None, defaults to 'dataset/recipe_site_traffic_2212.csv'.
        
    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    if file_path is None:
        # Construct the path relative to this file's directory
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, '..', 'dataset', 'recipe_site_traffic_2212.csv')
    
    # Normalize the path for cross-platform compatibility
    file_path = os.path.normpath(file_path)
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found at path: {file_path}") from e
