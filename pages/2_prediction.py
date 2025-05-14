import streamlit as st

st.set_page_config(page_title="Prediction", page_icon="📈")
st.header("Predictions")

st.markdown("#Prediction")

testing = st.slider("Data Testing", min_value=10, max_value=100)
