import streamlit as st
import pandas as pd

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Laboratorium Kimia",
    page_icon="🧪",
    layout="wide")

# ==========================
# CSS MODERN
# ==========================
st.markdown("""
<style>

.main {background: linear-gradient(135deg,#0f172a,#1e3a8a);}

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
""")

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

    st.title("🧪 Kuis Laboratorium Kimia")

    soal = [
        {
            "pertanyaan": "Alat yang digunakan untuk mengukur volume larutan secara teliti pada titrasi adalah...",
            "opsi": ["Erlenmeyer", "Buret", "Gelas Beker", "Corong"],
            "jawaban": "Buret"
        },

        {
            "pertanyaan": "Fungsi utama labu ukur adalah...",
            "opsi": [
                "Menyaring larutan",
                "Membuat larutan dengan volume tertentu",
                "Memanaskan larutan",
                "Mengukur massa"
            ],
            "jawaban": "Membuat larutan dengan volume tertentu"
        },

        {
            "pertanyaan": "Alat yang digunakan untuk mengambil sedikit cairan adalah...",
            "opsi": [
                "Pipet Tetes",
                "Corong",
                "Buret",
                "Kaki Tiga"
            ],
            "jawaban": "Pipet Tetes"
        },

        {
            "pertanyaan": "Pembakar spiritus berfungsi sebagai...",
            "opsi": [
                "Penyaring",
                "Pengukur volume",
                "Sumber panas",
                "Penyimpan larutan"
            ],
            "jawaban": "Sumber panas"
        },

        {
            "pertanyaan": "Tabung reaksi digunakan untuk...",
            "opsi": [
                "Tempat berlangsungnya reaksi",
                "Mengukur massa",
                "Menyaring larutan",
                "Menimbang sampel"
            ],
            "jawaban": "Tempat berlangsungnya reaksi"
        }
    ]

    jawaban_user = []

    progress = 0

    for i, item in enumerate(soal):

        st.subheader(f"Soal {i+1}")

        pilihan = st.radio(
            item["pertanyaan"],
            item["opsi"],
            key=i
        )

        jawaban_user.append(pilihan)

        progress += 1

        st.progress(progress / len(soal))

    st.divider()

    if st.button("📊 Selesai dan Lihat Nilai"):

        skor = 0

        st.subheader("Hasil Kuis")

        for i, item in enumerate(soal):

            if jawaban_user[i] == item["jawaban"]:
                skor += 20

                st.success(
                    f"Soal {i+1}: Benar ✅"
                )

            else:
                st.error(
                    f"Soal {i+1}: Salah ❌"
                )

                st.info(
                    f"Jawaban yang benar: {item['jawaban']}"
                )

        st.divider()

        st.metric(
            "Nilai Akhir",
            f"{skor}/100"
        )

        if skor >= 90:
            predikat = "A (Sangat Baik)"
            st.balloons()

        elif skor >= 80:
            predikat = "B (Baik)"

        elif skor >= 70:
            predikat = "C (Cukup)"

        else:
            predikat = "D (Perlu Belajar Lagi)"

        st.success(
            f"Predikat Anda: {predikat}"
        )

        st.progress(skor / 100)

        if skor == 100:
            st.balloons()
            st.success(
                "🎉 Selamat! Semua jawaban benar."
            )

    if st.button("🔄 Ulangi Kuis"):
        st.rerun()

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

