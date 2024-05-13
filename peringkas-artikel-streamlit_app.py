import streamlit as st
from io import StringIO
import requests
from transformers import pipeline
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup

st.header('Selamat Datang di Aplikasi Ringkkas.ID', divider='rainbow')
# Judul Aplikasi
st.title('Solusi Meringkas Cepat, Tepat, dan Akurat')

summarizer = pipeline("summarization")
# Input URL dari pengguna
url = st.text_input('Masukkan URL artikel yang ingin diringkas:')
if st.button('Ringkas'):
    # Mengambil teks dari URL
    article = requests.get(url).text
    # Membuat objek BeautifulSoup
    soup = BeautifulSoup(article, 'html.parser')
    # Mengumpulkan teks dari elemen paragraf
    paragraphs = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])
    
    # Melakukan peringkasan
    summary = summarizer(article_text, max_length=130, min_length=30, do_sample=False)

# Input File
uploaded_file = st.file_uploader("Unggah Dokumen (PDF atau DOCX)")

# Fungsi untuk membaca PDF
def read_pdf(file):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Fungsi untuk membaca DOCX
def read_docx(file):
    doc = Document(file)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

# Tombol Peringkas
if st.button('Peringkas'):
    if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        st.write(text)  # Tampilkan teks yang diambil
    elif uploaded_file:
        # Proses File
        if uploaded_file.name.endswith('.pdf'):
            text = read_pdf(uploaded_file)
            st.write(text)  # Tampilkan teks PDF
        elif uploaded_file.name.endswith('.docx'):
            text = read_docx(uploaded_file)
            st.write(text)  # Tampilkan teks DOCX
        else:
            st.error('Format file tidak didukung.')
    else:
        st.error('Silakan masukkan URL atau unggah file.')

# Fungsi peringkas teks (Contoh sederhana)
def summarize_text(text):
    # Implementasi algoritma peringkasan Anda di sini
    return text  # Sementara ini hanya mengembalikan teks asli

# Tampilkan hasil peringkasan
if st.button('Tampilkan Ringkasan'):
    summary = summarize_text(text)
    st.write(summary)
