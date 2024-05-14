import streamlit as st
from io import StringIO
import requests
from transformers import pipeline
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup
import re

st.header('Selamat Datang di Aplikasi Ringkas.ID')
# Judul Aplikasi
st.title('Solusi Meringkas Cepat, Tepat, dan Akurat')

# Fungsi untuk mengambil teks dari URL
def get_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            article_text = ' '.join(p.get_text() for p in paragraphs)
            return article_text
        else:
            return f"Error: Status code {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Menghapus data dalam tanda kurung siku
    text = re.sub(r'\[.*?\]', '', text)
    # Menghapus spasi ekstra
    text = re.sub(r'\s+', ' ', text)
    return text

# Input URL
url_input = st.text_input("Masukkan URL artikel")
  if url_input:
        # Proses URL
        text = get_text_from_url(url_input)
        text = clean_text(text)  # Membersihkan teks
        st.write(text)  # Tampilkan teks yang diambil
      
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
text = ''
if st.button('Lihat Teks'):
    elif uploaded_file:
        # Proses File
        if uploaded_file.name.endswith('.pdf'):
            text = read_pdf(uploaded_file)
            text = clean_text(text)  # Membersihkan teks
            st.write(text)  # Tampilkan teks PDF
        elif uploaded_file.name.endswith('.docx'):
            text = read_docx(uploaded_file)
            text = clean_text(text)  # Membersihkan teks
            st.write(text)  # Tampilkan teks DOCX
        else:
            st.error('Format file tidak didukung.')
    else:
        st.error('Silakan masukkan URL atau unggah file.')

# Fungsi peringkas teks
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Tampilkan hasil peringkasan
if st.button('Tampilkan Ringkasan'):
    if text:
        summary = summarize_text(text)
        st.write(summary)
    else:
        st.error('Silakan masukkan teks untuk diringkas.')
