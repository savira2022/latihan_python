import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung luas segitiga sederhana mengunakan streamlit
""")

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)

hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * alas * tinggi
    
    st.success(f"Luas segitiganya adalah {luas}")
    st.balloons()