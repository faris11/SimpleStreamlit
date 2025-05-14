import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Prediction", page_icon="📈")
st.header("Predictions")

#Load Dataset
df = pd.read_csv("model/iris.csv")
dataset = pd.read_csv('https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv')

#Tampilkan Dataframe
st.subheader("📁 Iris Dataset")
st.dataframe(dataset)

#Test Size
testing = st.slider("Data Testing", min_value=0, max_value=100, value=10)
st.write(f"Nilai yang dipilih: {testing}")
t_size = testing/100

#Select features and target
X = dataset.drop('variety', axis=1)
y = dataset['variety']

#Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size, random_state=42)

@st.cache_resource
def load_model(path):
    model = joblib.load(path)
    return model

model1 = load_model('model/decision_tree_model.joblib')

# Prediksi saat tombol ditekan
if st.button("Hasil"):
    y_pred1 = model1.predict(X_test)
    #Evaluate the models
    accuracy1 = accuracy_score(y_test, y_pred1)  
    st.success(f"Hasil Prediksi: {accuracy1}")
