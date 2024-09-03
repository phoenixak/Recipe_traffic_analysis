from scipy.stats import yeojohnson

def apply_transformations(df, columns):
    """Apply Yeo-Johnson transformations to specified columns."""
    df_transformed = df.copy()
    
    for column in columns:
        df_transformed[column] = yeojohnson(df_transformed[column])[0]
    
    return df_transformed
