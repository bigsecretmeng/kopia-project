import streamlit as st
from koneksi import koneksi
import pandas as pd


def halaman():
    st.header("📋 Dashboard Staff KOPIA")

    db = koneksi()
    cursor = db.cursor()

    # Ambil data sekali di awal
    cursor.execute("SELECT * FROM kopi")
    data_kopi = cursor.fetchall()

    cursor.execute(
        """
        SELECT 
            pelanggan.nama,
            kopi.nama_kopi,
            transaksi.jumlah,
            transaksi.total,
            transaksi.metode_pembayaran,
            kurir.nama_kurir
        FROM transaksi
        JOIN pelanggan ON transaksi.id_pelanggan = pelanggan.id_pelanggan
        JOIN kopi ON transaksi.id_kopi = kopi.id_kopi
        JOIN kurir ON transaksi.id_kurir = kurir.id_kurir
        """
    )
    data_transaksi = cursor.fetchall()

    # Siapkan dataframe untuk olah data & tampilan
    df_kopi = None
    df_transaksi = None

    if data_kopi:
        # kolom: id_kopi, nama_kopi, harga, stok
        df_kopi = pd.DataFrame(
            data_kopi,
            columns=["_id", "Menu Kopi", "Harga", "Stok"],
        )
        df_kopi.insert(0, "Nomor", range(1, len(df_kopi) + 1))
        df_kopi = df_kopi[["Nomor", "Menu Kopi", "Harga", "Stok"]]

    if data_transaksi:
        df_transaksi = pd.DataFrame(
            data_transaksi,
            columns=[
                "Pelanggan",
                "Pesanan",
                "Jumlah",
                "Total",
                "Metode Transaksi",
                "Nama Kurir Pengantar",
            ],
        )

    # ========================
    # RINGKASAN CEPAT (KPI)
    # ========================
    st.divider()

    col1, col2, col3 = st.columns(3)

    total_menu = len(df_kopi) if df_kopi is not None else 0
    total_stok = int(df_kopi["Stok"].sum()) if df_kopi is not None else 0

    total_transaksi = len(df_transaksi) if df_transaksi is not None else 0
    total_omzet = int(df_transaksi["Total"].sum()) if df_transaksi is not None else 0
    total_pelanggan = (
        int(df_transaksi["Pelanggan"].nunique()) if df_transaksi is not None else 0
    )

    with col1:
        st.metric("Jumlah Menu Kopi", f"{total_menu} menu")
        st.metric("Total Stok Kopi", f"{total_stok} cup")

    with col2:
        st.metric("Total Transaksi", f"{total_transaksi} transaksi")
        st.metric("Total Omzet", f"Rp {total_omzet:,}".replace(",", "."))

    with col3:
        st.metric("Jumlah Pelanggan Unik", f"{total_pelanggan} orang")

    st.divider()

    # ========================
    # DATA MENU KOPI
    # ========================
    st.subheader("☕ Data Menu Kopi")

    if df_kopi is not None:
        st.dataframe(
            df_kopi,
            use_container_width=True,
        )
    else:
        st.warning("Belum ada data kopi")

    st.divider()

    # ========================
    # DATA TRANSAKSI + FILTER
    # ========================
    st.subheader("🧾 Data Transaksi")

    if df_transaksi is not None:
        # Filter & pencarian
        c1, c2, c3 = st.columns(3)
        with c1:
            keyword = st.text_input("Cari pelanggan", placeholder="Nama pelanggan")
        with c2:
            metode_opsi = sorted(df_transaksi["Metode Transaksi"].unique())
            metode_pilih = st.multiselect(
                "Filter metode transaksi",
                options=metode_opsi,
                default=[],
            )
        with c3:
            kurir_opsi = sorted(df_transaksi["Nama Kurir Pengantar"].unique())
            kurir_pilih = st.multiselect(
                "Filter kurir pengantar",
                options=kurir_opsi,
                default=[],
            )

        df_view = df_transaksi.copy()

        if keyword:
            df_view = df_view[
                df_view["Pelanggan"].str.contains(keyword, case=False, na=False)
            ]

        if metode_pilih:
            df_view = df_view[df_view["Metode Transaksi"].isin(metode_pilih)]

        if kurir_pilih:
            df_view = df_view[df_view["Nama Kurir Pengantar"].isin(kurir_pilih)]

        st.dataframe(
            df_view,
            use_container_width=True,
        )
    else:
        st.warning("Belum ada transaksi")