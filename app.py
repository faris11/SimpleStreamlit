import streamlit as st

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
