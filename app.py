import streamlit as st
import pandas as pd

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Alat Laboratorium Kimia",
    page_icon="🧪",
    layout="wide")
# CUSTOM CSS
st.markdown("""
<style>
body {background-color: #0f172a;}

.main {background: linear-gradient(to right, #0f172a, #1e3a8a);color: white;}

.card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 15px rgba(0,255,255,0.5);
    transition: 0.3s;
    margin-bottom: 20px;}

.card:hover {transform: scale(1.03)}

.footer {text-align: center;
    padding: 20px;
    color: white;}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Dashboard")

menu = st.sidebar.radio(
    "Pilih Menu",
    [   "Home",
        "Daftar Alat",
        "Fungsi Alat",
        "Kuis Kimia",
        "Tentang Pembuat"])
# HOME

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

# DAFTAR ALAT

elif menu == "Daftar Alat":

    st.title("🔬 Daftar Alat Laboratorium")

    alat = [
        ("Gelas Beker", "Untuk mencampur larutan"),
        ("Erlenmeyer", "Untuk titrasi"),
        ("Buret", "Mengukur volume larutan"),
        ("Pipet Tetes", "Mengambil cairan"),
        ("Labu Ukur", "Membuat larutan"),
        ("Tabung Reaksi", "Tempat reaksi"),
        ("Corong", "Menyaring larutan"),
        ("Kaki Tiga", "Penyangga pemanasan"),
        ("Pembakar Spiritus", "Sumber api")
    ]

    cols = st.columns(3)

    for i, (nama, fungsi) in enumerate(alat):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
            <h3>🧪 {nama}</h3>
            <p>{fungsi}</p>
            </div>
            """, unsafe_allow_html=True)

# FUNGSI ALAT
# =========================
elif menu == "Fungsi Alat":

    st.title("📋 Fungsi Alat Laboratorium")

    data = {
        "Nama Alat": [
            "Gelas Beker",
            "Erlenmeyer",
            "Buret",
            "Pipet Tetes",
            "Labu Ukur"
        ],

        "Fungsi": [
            "Mencampur larutan",
            "Wadah titrasi",
            "Mengukur volume",
            "Mengambil cairan",
            "Membuat larutan"
        ],

        "Cara Penggunaan": [
            "Digunakan untuk mencampur",
            "Digoyangkan saat titrasi",
            "Dibaca volume akhirnya",
            "Ditekan bagian atasnya",
            "Diisi hingga tanda batas"
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)
# KUIS
# =========================
elif menu == "Kuis Kimia":

    st.title("📝 Kuis Laboratorium Kimia")

    score = 0

    q1 = st.radio(
        "1. Alat untuk titrasi adalah...",
        ["Pipet Tetes", "Erlenmeyer", "Corong"]
    )

    q2 = st.radio(
        "2. Fungsi buret adalah...",
        ["Mengukur volume", "Memanaskan", "Menyaring"]
    )

    q3 = st.radio(
        "3. Alat untuk pemanasan adalah...",
        ["Pembakar Spiritus", "Labu Ukur", "Buret"]
    )

    q4 = st.radio(
        "4. Pipet tetes digunakan untuk...",
        ["Mengambil cairan", "Memanaskan", "Menimbang"]
    )

    q5 = st.radio(
        "5. Tabung reaksi digunakan untuk...",
        ["Tempat reaksi", "Menimbang", "Mengukur massa"]
    )

    if st.button("Submit Jawaban"):

        if q1 == "Erlenmeyer":
            score += 20

        if q2 == "Mengukur volume":
            score += 20

        if q3 == "Pembakar Spiritus":
            score += 20

        if q4 == "Mengambil cairan":
            score += 20

        if q5 == "Tempat reaksi":
            score += 20

        st.success(f"Nilai Anda: {score}")

        if score >= 80:
            st.balloons()
            st.success(
                "Hebat! Anda memahami alat laboratorium kimia."
            )
        else:
            st.warning("Tetap semangat belajar kimia!")

# =========================
# TENTANG PEMBUAT
# =========================
elif menu == "Tentang Pembuat":

    st.title("👨‍🔬 Tentang Pembuat")

    st.markdown("""
    <div class="card">
    <h3>Data Pembuat</h3>
    <p><b>Nama:</b> Nama Anda</p>
    <p><b>Jurusan:</b> Kimia</p>
    <p><b>Tujuan:</b> Membuat media pembelajaran alat laboratorium kimia.</p>
    <p><b>GitHub:</b> github.com/usernameanda</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div class="footer">
© 2026 Website Laboratorium Kimia | Dibuat dengan Streamlit 🧪
</div>
""", unsafe_allow_html=True)

