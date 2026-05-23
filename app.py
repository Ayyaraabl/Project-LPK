import streamlit as st
import pandas as pd

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Alat Laboratorium Kimia",
    page_icon="🧪",
    layout="wide")
# CUSTOM CSS
st.markdown("""
<style>
body {background-color: #0f172a;}

.main {background: linear-gradient(to right, #0f172a, #1e3a8a);color: white;}

h1, h2, h3 {color: #ffffff;text-shadow: 0px 0px 10px cyan;}

.card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 15px rgba(0,255,255,0.5);
    transition: 0.3s;
    margin-bottom: 20px;}

.card:hover {transform: scale(1.03);
    box-shadow: 0 0 25px cyan;}

.footer {text-align: center;
    padding: 20px;
    color: white;}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧪 Alat Kimia")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Home",
        "Daftar Alat",
        "Fungsi Alat",
        "Kuis Kimia",
        "Tentang Pembuat"
    ]
)
# HOME
# =========================
if menu == "Home":

    st.title("🧪 Pengenalan Alat-Alat Laboratorium Kimia")

    st.markdown("""
    <div class="card">
    <h3>Belajar Alat Lab Yuk!</h3>
    <p>
    Website ini dibuat untuk membantu mempelajari berbagai alat laboratorium kimia
    beserta fungsi dan cara penggunaannya.
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Jumlah Alat", "9")
    col2.metric("Kategori", "Laboratorium")
    col3.metric("Status", "Aktif")

    st.image("https://share.google/G8moOGxuzdE7JsisA")


    st.success("Kimia adalah ilmu yang penuh eksperimen dan ketelitian.")
