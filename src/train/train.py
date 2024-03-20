import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def getData():
    data = pd.read_csv("data.csv")
    X = data.drop(["PRICE"], axis=1)
    y = data["PRICE"]
    return X, y

def trainModel(X, y):
    reg = RandomForestRegressor()
    reg.fit(X, y)
    return reg

def saveModel(model):
    joblib.dump(model, "../app/boston_housing_prediction_test.joblib")

if __name__ == "__main__":
    X, y = getData()
    regModel = trainModel(X, y)
    saveModel(regModel) 
