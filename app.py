import streamlit as st
import json
import os

DATA_PATH = "data/books.json"

st.set_page_config(page_title="Book Crawler App", layout="wide")
st.title("📚 Book Crawler Search App")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("Cari judul buku:")

# Filter data
if query:
    filtered = [item for item in data if query.lower() in item.get("title", "").lower()]
    st.markdown(f"### Hasil: {len(filtered)} ditemukan")
else:
    filtered = data
    st.markdown("### Semua hasil")

# Tampilkan hasil
for item in filtered:
    title = item.get("title", "Tanpa Judul")
    link = item.get("link", "#")
    price = item.get("price", "-")
    stock = item.get("availability", "-")

    st.markdown(f"[📘 \"{title}\"]({link})")
    st.markdown(f"💰 Harga: `{price}`")
    st.markdown(f"📦 Stok: `{stock}`")
    st.markdown("---")
