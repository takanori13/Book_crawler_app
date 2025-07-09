# app.py
import streamlit as st
import json
import os

DATA_PATH = "data/results.json"

st.set_page_config(page_title="Web Crawler Search", layout="wide")
st.title("🔍 Web Crawler Search App")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
    st.stop()

# Input pencarian
query = st.text_input("Cari kutipan atau nama penulis:", "")

# Filter data
if query:
    filtered = [item for item in data if query.lower() in item["text"].lower()
                or query.lower() in item["author"].lower()]
    st.markdown(f"### Hasil: {len(filtered)} ditemukan")
else:
    filtered = data
    st.markdown("### Semua hasil")

# Tampilkan hasil
for item in filtered:
    # Tampilkan judul sebagai link yang bisa diklik
    st.markdown(f"[📘 \"{item['text']}\"]({item['url']}) – *{item['author']}*")
    st.markdown(f"`Tags:` {', '.join(item['tags'])}")
    st.markdown("---")
