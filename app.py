import streamlit as st

from src.agents import run_healthcare_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("🏥 AI Autonomous Healthcare Diagnosis Intelligence Platform")

query = st.text_input("Ask Clinical Intelligence Insight")

if st.button("Analyze Patient Health"):

    df, prediction, risk, explanation = run_healthcare_ai()

    st.subheader("📊 Patient Healthcare Dataset")
    st.dataframe(df)

    st.subheader("📈 Disease Risk Forecast")
    st.write(f"Predicted Clinical Risk Score: {prediction:.2f}")

    st.subheader("⚠️ Disease Risk Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.line_chart(df["glucose"])

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Medical Intelligence Insights")

        for i in insights:
            st.write(i)