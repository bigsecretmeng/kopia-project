import streamlit as st


def tampilkan_struk(nama, kopi, jumlah, total, kurir, metode):
    st.markdown(
        f"""
        <div class="struk-box">
            <h3>🧾 STRUK PEMBELIAN KOPIA</h3>
            <div class="struk-row">
                <span class="struk-label">Nama Pelanggan</span>
                <span class="struk-value">{nama}</span>
            </div>
            <div class="struk-row">
                <span class="struk-label">Menu Kopi</span>
                <span class="struk-value">{kopi}</span>
            </div>
            <div class="struk-row">
                <span class="struk-label">Jumlah</span>
                <span class="struk-value">{jumlah}</span>
            </div>
            <div class="struk-row">
                <span class="struk-label">Total Bayar</span>
                <span class="struk-value">Rp {total}</span>
            </div>
            <div class="struk-row">
                <span class="struk-label">Metode Pembayaran</span>
                <span class="struk-value">{metode}</span>
            </div>
            <div class="struk-row">
                <span class="struk-label">Kurir Pengantar</span>
                <span class="struk-value">{kurir}</span>
            </div>
            <p class="struk-footer">
                Terima kasih sudah memesan di KOPIA ☕
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )