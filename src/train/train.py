"""
Training a Random Forest Regression model on the boston housing data set.
"""
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

dirname = os.path.dirname(os.path.abspath(__file__))

def get_data():
    """
    Extracting data from data.csv file.

    Returns:
        x : The features.
        y : The labels.
    """
    data_path = str(dirname)+"/data.csv"
    data = pd.read_csv(data_path)
    x = data.drop(["PRICE"], axis=1)
    y = data["PRICE"]
    return x, y

def train_model(x, y):
    """
    Train the Random Forest Regression model.

    Args:
        x : The features.
        y : The labels.

    Returns:
        reg : The model.
    """
    reg = RandomForestRegressor()
    reg.fit(x, y)
    return reg

def save_model(model):
    """
    Save the model to file.

    Args:
        model : The model
    """
    model_path = str(dirname)+"/../app/boston_housing_prediction_test.joblib"
    joblib.dump(model, model_path)

if __name__ == "__main__":
    print("Starting model training...")
    print("-Fetching data...")
    features, labels = get_data()
    print("-Data fetched successfully!")
    print("-Training model...")
    reg_model = train_model(features, labels)
    print("-Model Trained successfully!")
    print("-Saving model...")
    save_model(reg_model)
    print("-Model saved successfully!")
    print("Model training ended")
