import streamlit as st

st.set_page_config(page_title="Prediction", page_icon="📈")
st.header("Predictions")

testing = st.slider("Data Testing", min_value=0, max_value=100, value=10)
st.write(f"Nilai yang dipilih: {testing}")

# Select features and target for the iris dataset
X = dataset.drop('variety', axis=1)
y = dataset['variety']

t_size = testing/100
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size, random_state=42)
