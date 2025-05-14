import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Aplikasi Streamlit Sederhana", layout="centered")

st.title("🎈 Selamat datang di Aplikasi Streamlit Sederhana!")
st.write("Aplikasi ini dibuat untuk demonstrasi deploy langsung dari GitHub.")

# Input interaktif
name = st.text_input("Siapa nama Anda?")
if name:
    st.success(f"Halo, {name}! 👋")

# Contoh slider
value = st.slider("Pilih nilai", 0, 100, 50)
st.write(f"Nilai yang dipilih: {value}")

df = pd.read_csv("model/iris.csv")

# Tampilkan dataframe
st.subheader("📁 Isi Data Iris")
st.dataframe(df)

# Load model
@st.cache_resource
def load_model():
    with open("model/decision_tree_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.write("Masukkan data input di bawah ini:")

# Input fitur
seplen = st.number_input("Sepal Length", min_value=0, max_value=8, value=2)
sepwid = st.number_input("Sepal Width", min_value=0, max_value=8, value=2)
petlen = st.number_input("Petal Length", min_value=0, max_value=8, value=2)
petwid = st.number_input("Petal Width", min_value=0, max_value=8, value=2)

# Prediksi saat tombol ditekan
if st.button("Prediksi"):
    input_data = pd.DataFrame([[seplen, sepwid, petlen, petwid]],
                              columns=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"])
    
    hasil = model.predict(input_data)
    st.success(f"Hasil Prediksi: {hasil[0]}")
