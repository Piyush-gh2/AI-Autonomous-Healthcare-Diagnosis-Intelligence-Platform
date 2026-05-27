from src.loader import load_data
from src.forecasting import forecast_health_risk
from src.diagnosis_engine import detect_health_risk
from src.explainable_ai import explain_risk

def run_healthcare_ai():

    df = load_data()

    prediction = forecast_health_risk(df)

    latest_glucose = df["glucose"].iloc[-1]
    latest_oxygen = df["oxygen_level"].iloc[-1]
    latest_heart = df["heart_rate"].iloc[-1]

    risk = detect_health_risk(
        latest_glucose,
        latest_oxygen,
        latest_heart
    )

    explanation = explain_risk(
        latest_glucose,
        latest_oxygen
    )

    return df, prediction, risk, explanation