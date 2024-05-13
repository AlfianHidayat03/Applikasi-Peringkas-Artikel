import streamlit as st
from transformers import pipeline

# Inisialisasi pipeline peringkasan
summarizer = pipeline("summarization")

st.title('Aplikasi Peringkas Artikel dengan Streamlit')

st.write("Masukkan teks artikel di bawah ini dan aplikasi akan menghasilkan ringkasan.")

# Text area untuk input artikel
input_text = st.text_area("Teks Artikel", height=300)

# Tombol untuk melakukan peringkasan
if st.button('Ringkas'):
    if input_text:
        # Melakukan peringkasan
        summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
        # Menampilkan hasil ringkasan
        st.subheader('Ringkasan Artikel:')
        st.write(summary[0]['summary_text'])
    else:
        st.error('Silakan masukkan teks artikel untuk diringkas.')
