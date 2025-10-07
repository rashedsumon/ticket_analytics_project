import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning: remove duplicates, handle missing values.
    """
    df = df.drop_duplicates()
    df = df.fillna(0)
    # Additional transformations can be added here
    return df
