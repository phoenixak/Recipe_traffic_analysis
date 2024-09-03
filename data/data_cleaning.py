import pandas as pd

def clean_data(df):
    """Clean and preprocess the data."""
    # Remove duplicates
    df = df.drop_duplicates(subset='recipe')

    # Clean 'servings' column
    if df['servings'].dtype == object:
        df['servings'] = df['servings'].str.replace(" as a snack", "").astype(int)
    
    # Convert 'high_traffic' to boolean
    df['high_traffic'] = df['high_traffic'].apply(lambda x: True if isinstance(x, str) and x.lower() == "high" else False)

    # Clean 'category' column and convert to categorical
    df['category'] = df['category'].str.replace(" Breast", "").astype('category')

    # Drop rows with missing values
    df = df.dropna().reset_index(drop=True)

    return df
