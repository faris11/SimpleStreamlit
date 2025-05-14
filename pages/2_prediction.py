import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Prediction", page_icon="📈")
st.header("Predictions")

df = pd.read_csv("model/iris.csv")
dataset = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

# Tampilkan dataframe
st.subheader("📁 Iris Dataset")
st.dataframe(dataset)

testing = st.slider("Data Testing", min_value=0, max_value=100, value=10)
st.write(f"Nilai yang dipilih: {testing}")

# Select features and target for the iris dataset
X = dataset.drop('variety', axis=1)
y = dataset['variety']

t_size = testing/100
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size, random_state=42)
