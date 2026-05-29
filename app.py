import streamlit as st
import pandas as pd

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Laboratorium Kimia",
    page_icon="🧪",
    layout="wide"
)

# ==========================
# CSS MODERN
# ==========================
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#0f172a,#1e3a8a);
}

.title {
    text-align:center;
    color:white;
    padding:15px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:15px;
    backdrop-filter: blur(8px);
    border:1px solid rgba(255,255,255,0.2);
}

.card:hover{
    transform:scale(1.02);
}

.footer{
    text-align:center;
    margin-top:40px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# DATABASE ALAT
# ==========================
alat_data = {
    "Nama": [
        "Gelas Beker",
        "Erlenmeyer",
        "Buret",
        "Pipet Tetes",
        "Labu Ukur",
        "Tabung Reaksi",
        "Corong",
        "Kaki Tiga",
        "Pembakar Spiritus"
    ],

    "Fungsi": [
        "Mencampur dan memanaskan larutan",
        "Wadah titrasi",
        "Mengukur volume titran",
        "Mengambil cairan dalam jumlah kecil",
        "Membuat larutan standar",
        "Tempat berlangsungnya reaksi",
        "Menyaring larutan",
        "Penyangga saat pemanasan",
        "Sumber panas"
    ]
}

df = pd.DataFrame(alat_data)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2784/2784445.png",
    width=120
)

st.sidebar.title("🔬 Menu")

menu = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "Beranda",
        "Daftar Alat",
        "Pencarian Alat",
        "Kuis",
        "Tentang"
    ]
)

# ==========================
# BERANDA
# ==========================
if menu == "Beranda":

    st.markdown(
        "<h1 class='title'>🧪 Laboratorium Kimia Interaktif</h1>",
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1532187643603-ba119ca4109e",
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Jumlah Alat", len(df))
    col2.metric("Kategori", "Laboratorium")
    col3.metric("Status", "Aktif")

    st.markdown("""
    <div class="card">
    <h3>Selamat Datang</h3>
    <p>
    Website ini berisi pengenalan alat-alat laboratorium kimia,
    fungsi alat, dan kuis interaktif untuk menguji pemahaman Anda.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# DAFTAR ALAT
# ==========================
elif menu == "Daftar Alat":

    st.title("📋 Daftar Alat Laboratorium")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# ==========================
# PENCARIAN ALAT
# ==========================
elif menu == "Pencarian Alat":

    st.title("🔎 Cari Alat Laboratorium")

    keyword = st.text_input(
        "Masukkan nama alat"
    )

    if keyword:

        hasil = df[
            df["Nama"].str.contains(
                keyword,
                case=False
            )
        ]

        if len(hasil) > 0:
            st.success("Alat ditemukan")
            st.dataframe(
                hasil,
                use_container_width=True,
                hide_index=True
            )
        else:
            st.error("Alat tidak ditemukan")

# ==========================
# KUIS
# ==========================
elif menu == "Kuis":

    st.title("📝 Kuis Kimia")

    score = 0

    q1 = st.radio(
        "1. Alat yang digunakan pada titrasi?",
        ["Corong", "Erlenmeyer", "Tabung Reaksi"]
    )

    q2 = st.radio(
        "2. Fungsi buret?",
        ["Mengukur volume larutan",
         "Menyaring larutan",
         "Memanaskan larutan"]
    )

    q3 = st.radio(
        "3. Fungsi pipet tetes?",
        ["Mengambil cairan",
         "Mengukur massa",
         "Memanaskan"]
    )

    if st.button("Periksa Jawaban"):

        if q1 == "Erlenmeyer":
            score += 1

        if q2 == "Mengukur volume larutan":
            score += 1

        if q3 == "Mengambil cairan":
            score += 1

        nilai = score / 3 * 100

        st.subheader(f"Nilai Anda : {nilai:.0f}")

        if nilai == 100:
            st.balloons()
            st.success("Sempurna 🎉")
        elif nilai >= 70:
            st.success("Bagus 👍")
        else:
            st.warning("Perlu belajar lagi 📚")

# ==========================
# TENTANG
# ==========================
elif menu == "Tentang":

    st.title("👨‍🔬 Tentang Pembuat")

    st.markdown("""
    <div class="card">
    <h3>Profil</h3>

    Nama : Nama Anda

    Program Studi : Kimia

    Tujuan :
    Membuat media pembelajaran interaktif
    mengenai alat laboratorium kimia.

    Teknologi :
    Python + Streamlit
    </div>
    """, unsafe_allow_html=True)

# ==========================
# FOOTER
# ==========================
st.markdown("""
<div class='footer'>
© 2026 Laboratorium Kimia Interaktif | Dibuat dengan Streamlit 🧪
</div>
""", unsafe_allow_html=True)

