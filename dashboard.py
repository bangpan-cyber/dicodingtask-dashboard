import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

st.set_page_config(page_title="bangpanj webpage", layout="wide")
img_tren = Image.open("img/tren order.png")

with st.container():
    st.title('Laporan Analisa Dataset Publik E-Commerce Olist :bar_chart:')

with st.container():
    st.write("---")
    st.header("Berdasarkan data-data yang disediakan oleh e-commerce bernama Olist, saya mencoba untuk membuat analisa berdasarkan 2 pertanyaan bisnis.")
    st.write("##")
    st.write(
            """
            Dan, berikut adalah dua pertanyaan bisnisnya:

            - "Bagaimana performa logistik Olist berubah dari tahun 2016 hingga 2018, apakah ada peningkatan atau penurunan dalam waktu pengiriman?".
            - "Kategori produk apa yang paling banyak dan yang paling sedikit terjual?
            """
    )

with st.container():
    st.write("---")
    st.header('Trend in Order Volume over Time')
    st.write("##")
    image_column, text_column = st.columns((2, 1))
    with image_column:
        st.image(img_tren)
    with text_column:
        st.write("##")
        if st.button("Kesimpulan analisa tren"):
            st.write(
            """
            Dengan melihat analisa tren jumlah pesanan tersebut, bisa diambil kesimpulan:
            - Jumlah pesanan menunjukkan tren peningkatan pada periode tertentu. Terlihat dari data, mulai awal tahun 2017 hingga bulan Juli 2018 mengalami tren naik.
            Puncaknya terjadi di periode bulan Oktober hingga November 2017. Namun menjelang bulan Oktober 2018, tren menurun drastis. Dengan ini, pertumbuhan bisnis sempat mengalami kondisi yang positif, sebelum menjelan bulan Oktober tahun 2018.
            """)

with st.container():
    st.write("---")
    st.header('Order Status Report')
    st.write("##")
    the_bar, txt_column = st.columns((2, 1))
    with the_bar:
        orders = pd.read_csv('olist_order_df.csv')

        status_counts = orders['order_status'].value_counts().reset_index()
        fig, ax = plt.subplots(figsize=(37, 17))

        sns.barplot(x='index', y='order_status', data=status_counts, ax=ax, palette='viridis')
        ax.set_title('Order Status Distribution', fontsize=50)
        ax.set_xlabel('Status', fontsize=35)
        ax.set_ylabel('Number of Orders', fontsize=35)
        ax.tick_params(axis='x', rotation=25, labelsize=25)
        ax.tick_params(axis='y', labelsize=25)
        st.pyplot(fig)
    with txt_column:
        if st.button("Kesimpulan analisa laporan status order"):
            st.write(
            """
            Dengan melihat analisa laporan status order, bisa diambil kesimpulan:
            - Distribusi status pesanan menunjukkan mayoritas pesanan dalam kondisi "delivered" atau "shipped," yang menandakan bahwa sebagian besar pesanan berhasil dikirim.
            """)

with st.container():
    st.write("---")
    st.header('Best and Worst Performing Product Category')
    st.write("##")
    

combined_data = pd.read_csv('olist_sales_df.csv')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(37, 17))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x='order_item_id', y='product_category_name_english', data=combined_data.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title('Best performing product category', loc='center', fontsize=40)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)

sns.barplot(x='order_item_id', y='product_category_name_english', data=combined_data.sort_values(by='order_item_id', ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title('Worst performing product category', loc='center', fontsize=40)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
st.pyplot(fig)

if st.button("Kesimpulan analisa kateori produk terbaik & terburuk"):
    st.write(
            """           
            Kesimpulan dari analisa kategori produk yang paling banyak dan yang paling sedikit terjual adalah sebagai berikut.
            1. Kategori produk paling banyak terjual:
            Dari visualisasi data, kita dapat melihat kategori produk dengan penjualan terbanyak. Melalui bar chart, kita dapat mengidentifikasi kategori produk yang mendominasi dalam jumlah penjualan, yaitu kategori produk 'bed_bath_table'.
            2. Kategori produk paling sedikit terjual:
            Dari visualisasi datanya, kategori produk 'security_and_services' adalah paling sedikit terjual.
           """
        )
st.caption('Copyright (c) Dicoding 2023')
