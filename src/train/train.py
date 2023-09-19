import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

if __name__ == "__main__":
    # Load training data
    train_data = pd.read_csv("/opt/ml/input/data/train/train.csv")
    train_x = train_data.drop("target", axis=1)
    train_y = train_data["target"]

    # Retrieve hyperparameters from environment variables
    C = float(os.environ.get("C", 1.0))  # Regularization strength; default is 1.0
    max_iter = int(
        os.environ.get("max_iter", 100)
    )  # Maximum number of iterations; default is 100

    # Train logistic regression model
    model = LogisticRegression(C=C, max_iter=max_iter)
    model.fit(train_x, train_y)

    # Save the model
    joblib.dump(model, "/opt/ml/model/model.pkl")
