def explain_risk(glucose, oxygen):

    if glucose > 180:
        return "Clinical alert generated due to elevated glucose levels."

    elif oxygen < 90:
        return "Clinical alert generated due to low oxygen saturation."

    else:
        return "Patient vitals appear operationally stable."