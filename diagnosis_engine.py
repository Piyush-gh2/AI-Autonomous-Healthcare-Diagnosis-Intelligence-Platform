def detect_health_risk(glucose, oxygen, heart_rate):

    if glucose > 180:
        return "High Diabetes Risk"

    elif oxygen < 90:
        return "Respiratory Risk Alert"

    elif heart_rate > 110:
        return "Cardiac Risk Warning"

    else:
        return "Patient Condition Stable"