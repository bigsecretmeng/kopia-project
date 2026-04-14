import streamlit as st
import pelanggan
import staff

st.set_page_config(page_title="KOPIA Coffee", layout="wide")

st.markdown("""
<style>

/* background utama dengan gradasi kopi */
.stApp {
    background: radial-gradient(circle at top left, #fdf6ec 0%, #f3ddc0 40%, #e2c3a3 100%);
}

/* sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b2618 0%, #24150e 100%);
}

/* judul & heading */
h1, h2, h3 {
    color: #3b2618 !important;
}

p, label {
    color: #4a3323 !important;
}

/* container utama form */
div[data-testid="stVerticalBlock"] > div:nth-child(2) {
    background-color: rgba(255, 255, 255, 0.76);
    border-radius: 18px;
    padding: 24px 28px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
}

/* kotak input */
.stTextInput input,
.stNumberInput input {
    background-color: #fffaf4;
    color: #2c1a10;
    border-radius: 10px;
    border: 1px solid #e0c2a2;
}

/* selectbox */
div[data-baseweb="select"] {
    background-color: #fffaf4;
    color: #2c1a10;
    border-radius: 10px;
    border: 1px solid #e0c2a2;
}

/* tombol utama */
.stButton button {
    background: linear-gradient(135deg, #8b5e3c, #c28b5a);
    color: white;
    border-radius: 999px;
    border: none;
    padding: 0.5rem 1.8rem;
    font-weight: 600;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.25);
}

.stButton button:hover {
    background: linear-gradient(135deg, #70482c, #a06d45);
}

/* tabel data (Data Menu Kopi & Data Transaksi) - komponen DataFrame baru */
div[data-testid="stDataFrame"] {
    background-color: rgba(255, 250, 244, 0.98);
    border-radius: 18px;
    padding: 12px 16px;
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.16);
}

/* header kolom */
div[data-testid="stDataFrame"] div[role="columnheader"] {
    justify-content: center;
}

/* sel data */
div[data-testid="stDataFrame"] div[role="gridcell"] {
    justify-content: center;
}

/* kotak hasil / struk */
.struk-box {
    background: linear-gradient(135deg, #fdf5ec, #f1e0cf);
    border-radius: 18px;
    padding: 24px 28px;
    border: 1px solid #e0c9a6;
    box-shadow: 0 14px 30px rgba(0, 0, 0, 0.12);
    max-width: 520px;
    margin: 28px auto 10px auto;
}

.struk-box h3 {
    margin-top: 0;
    margin-bottom: 16px;
    text-align: center;
    color: #4a2c18;
}

.struk-row {
    display: flex;
    justify-content: space-between;
    margin: 6px 0;
    font-size: 0.95rem;
}

.struk-label {
    font-weight: 600;
    color: #4a2c18;
}

.struk-value {
    color: #3b2a1a;
}

.struk-footer {
    margin-top: 18px;
    text-align: center;
    font-style: italic;
    color: #6b4a2c;
}

</style>
""", unsafe_allow_html=True)

st.title("☕ Sistem Pemesanan Kopi KOPIA")

menu = st.sidebar.selectbox(
    "Menu",
    ["Pelanggan", "Staff"]
)

if menu == "Pelanggan":
    pelanggan.halaman()

elif menu == "Staff":
    staff.halaman()