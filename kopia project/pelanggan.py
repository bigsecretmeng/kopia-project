import streamlit as st
from koneksi import koneksi
import random
import struk

def halaman():

    st.header("Pesan Kopi KOPIA")

    db = koneksi()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM kopi")
    data = cursor.fetchall()

    daftar_kopi = {}

    for d in data:
        daftar_kopi[d[1]] = d[2]

    nama = st.text_input("Nama Pelanggan")
    alamat = st.text_input("Alamat")

    kopi = st.selectbox("Pilih Kopi", list(daftar_kopi.keys()))

    jumlah = st.number_input("Jumlah", 1)

    harga = daftar_kopi[kopi]
    total = harga * jumlah

    st.write("Total Bayar :", total)

    metode = st.selectbox(
        "Metode Pembayaran",
        ["Transfer Bank", "DANA"]
    )

    if metode == "Transfer Bank":
        st.write("Transfer ke Bank BCA")
        st.write("No Rekening: 1234567890")
        st.write("A/N Kopia Coffee")

    elif metode == "DANA":
        st.write("Transfer ke DANA")
        st.write("No DANA: 081234567890")

    if st.button("Pesan Sekarang"):

        cursor.execute(
        "INSERT INTO pelanggan (nama,alamat) VALUES (%s,%s)",
        (nama,alamat))

        id_pelanggan = cursor.lastrowid

        cursor.execute(
        "SELECT id_kopi FROM kopi WHERE nama_kopi=%s",(kopi,))
        id_kopi = cursor.fetchone()[0]

        cursor.execute("SELECT id_kurir,nama_kurir FROM kurir")
        data_kurir = cursor.fetchall()

        kurir = random.choice(data_kurir)

        id_kurir = kurir[0]
        nama_kurir = kurir[1]

        cursor.execute(
        "INSERT INTO transaksi (id_pelanggan,id_kopi,jumlah,total,id_kurir,metode_pembayaran) VALUES (%s,%s,%s,%s,%s,%s)",
        (id_pelanggan,id_kopi,jumlah,total,id_kurir,metode)
        )

        db.commit()

        st.success("Pesanan berhasil!")

        struk.tampilkan_struk(
            nama,
            kopi,
            jumlah,
            total,
            nama_kurir,
            metode
        )