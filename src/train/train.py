"""
Training a Random Forest Regression model on the boston housing data set.
"""
import logging
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

logger = logging.getLogger(__name__)

def get_data():
    """
    Extracting data from data.csv file.

    Returns:
        x : The features.
        y : The labels.
    """
    data = pd.read_csv("data.csv")
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
    joblib.dump(model, "../app/boston_housing_prediction_test.joblib")

if __name__ == "__main__":
    logger.info("Starting model training...")
    logger.info("-Fetching data...")
    features, labels = get_data()
    logger.info("-Data fetched successfully!")
    logger.info("-Training model...")
    reg_model = train_model(features, labels)
    logger.info("-Model Trained successfully!")
    logger.info("-Saving model...")
    save_model(reg_model)
    logger.info("-Model saved successfully!")
    logger.info("Model training ended.")
