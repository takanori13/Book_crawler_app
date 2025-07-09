import streamlit as st
import pandas as pd
import json

# Load data
with open("data/books.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Streamlit UI
st.title("Book Search App 📚")

search = st.text_input("Cari judul buku:")

if search:
    results = df[df['title'].str.contains(search, case=False)]
else:
    results = df

st.write(f"Hasil: {len(results)} buku ditemukan")
st.dataframe(results)
