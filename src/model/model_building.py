import numpy as np
import pandas as pd
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
import yaml

def load_params(params_path: str) -> int:
    try:
        with open(params_path,"r") as file:
            params = yaml.safe_load(file)
        return params["model_building"]["n_estimators"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {params_path}: {e}")

# n_estimators = yaml.safe_load(open("params.yaml","r"))["model_building"]["n_estimators"]

def load_data(data_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(data_path)
    except Exception as e:
        raise Exception(f"Error Loading data from {data_path}: {e}")

# train_data = pd.read_csv("./data/processed/train_processed.csv")

# x_train = train_data.iloc[:,0:-1].values
# y_train = train_data.iloc[:,-1].values

def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame,pd.Series]:
    try:
        x = data.drop(columns=["Potability"], axis=1)
        y = data["Potability"]
        return x,y
    except Exception as e:
        raise Exception(f"Error Preparing Data: {e}")

# x_train = train_data.drop(columns=["Potability"], axis=1)
# y_train = train_data["Potability"]

def train_model(x: pd.DataFrame, y: pd.Series, n_estimators: int) -> RandomForestClassifier:
    try:
        model = RandomForestClassifier(n_estimators=n_estimators)
        model.fit(x,y)
        return model
    except Exception as e:
        raise Exception(f"Error Training Model: {e}")
    
def save_model(model: RandomForestClassifier, model_name: str) -> None:
    try:
        with open(model_name,"wb") as file:
            pickle.dump(model,file)
    except Exception as e:
        raise Exception(f"Error saving model to {model_name}: {e}")

# pickle.dump(model,open("model.pkl","wb"))

def main():
    try:
        params_path = "params.yaml"
        data_path = "./data/processed/train_processed.csv"
        model_name = "models/model.pkl"

        n_estimators = load_params(params_path)
        train_data = load_data(data_path)
        x_train, y_train = prepare_data(train_data)
        model = train_model(x_train,y_train,n_estimators)
        save_model(model,model_name)
    except Exception as e:
        raise Exception(f"An Error Occureed : {e}")

if __name__ == "__main__":
    main()