import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(df: pd.DataFrame):
    """
    Train a simple linear regression model to predict ticket demand
    """
    if 'Tickets_Sold' in df.columns and 'Price' in df.columns:
        X = df[['Price']]  # Example feature
        y = df['Tickets_Sold']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    else:
        return None

def predict_demand(model, df: pd.DataFrame):
    if model is None:
        return pd.DataFrame({"Error": ["Model could not be trained"]})
    X = df[['Price']]
    df['Predicted_Tickets'] = model.predict(X)
    return df[['Price', 'Predicted_Tickets']]
