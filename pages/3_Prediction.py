import streamlit as st

st.set_page_config(page_title="Prediction", page_icon="📈")
st.header("Prediction")

st.write("Make a prediction using a new data")

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
