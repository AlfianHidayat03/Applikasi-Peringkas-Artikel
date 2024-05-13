import streamlit as st
from io import StringIO
import re
from transformers import pipeline
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup

st.header('Selamat Datang di Aplikasi Ringkas.ID', divider='rainbow')
# Judul Aplikasi
st.title('Solusi Meringkas Cepat, Tepat, dan Akurat')

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus data dalam tanda kurung siku
    text = re.sub(r'\[.*?\]', '', text)
    # Menghapus spasi ekstra
    text = re.sub(r'\s+', ' ', text)
    return text

# Menggunakan Streamlit untuk input URL
url_input = st.text_input('Masukkan URL Artikel')

# Fungsi untuk mengambil teks dari URL
def get_text_from_url(url_input):
    response = requests.get(url_input)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Menggabungkan teks dari semua paragraf
    article_text = ' '.join([p.text for p in soup.find_all('p')])
    # Membersihkan teks
    cleaned_text = clean_text(article_text)
    return cleaned_text

# Menampilkan teks yang telah dibersihkan
if st.button('Dapatkan Teks'):
    article_text = get_text_from_url(url_input)
    st.text_area('Teks Artikel:', article_text, height=250)



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
