import streamlit as st
import json
import os

# Path ke data
DATA_PATH = "data/books.json"

# Konfigurasi halaman
st.set_page_config(
    page_title="📚 Book Crawler Search",
    layout="wide"
)

# Judul utama
st.markdown("<h1 style='text-align: center;'>📚 Book Crawler Search App</h1>", unsafe_allow_html=True)
st.write("---")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.error("❌ Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("🔍 Cari judul buku:")

# Filter data
if query:
    filtered = [item for item in data if query.lower() in item.get("title", "").lower()]
    st.success(f"Hasil: {len(filtered)} ditemukan")
else:
    filtered = data
    st.info(f"Menampilkan semua hasil ({len(filtered)} buku)")

st.write("---")

# Tampilkan hasil
for item in filtered:
    title = item.get("title", "Tanpa Judul")
    price = item.get("price", "Tidak diketahui")
    stock = item.get("availability", "Tidak diketahui")
    link = item.get("link", "#")

    with st.container():
        st.markdown(f"<h4><a href='{link}' target='_blank' style='text-decoration: none; color: #1f77b4;'>📘 {title}</a></h4>", unsafe_allow_html=True)
        st.markdown(f"<b>💰 Harga:</b> {price} &nbsp;&nbsp;&nbsp; <b>📦 Stok:</b> {stock}", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
