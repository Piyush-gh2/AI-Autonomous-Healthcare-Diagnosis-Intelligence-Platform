from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_health_risk(df):

    df["t"] = range(1, len(df)+1)

    X = df[["t"]]
    y = df["glucose"]

    model = LinearRegression()
    model.fit(X, y)

    next_patient = np.array([[len(df)+1]])

    prediction = model.predict(next_patient)

    return prediction[0]