import streamlit as st
from io import StringIO
import requests
from transformers import pipeline
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup
from gensim.summarization import summarize
import re

st.header('Selamat Datang di Aplikasi Ringkas.ID', divider='rainbow')
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

# Fungsi untuk meringkas teks
def summarize_text(text):
    # Ini hanya placeholder untuk fungsi meringkas teks
    # Anda bisa menggunakan library seperti nltk atau gensim untuk meringkas teks
    # Atau Anda bisa mengembangkan algoritma meringkas teks sendiri
    summarized_text = text[:500] + '...'  # Contoh sederhana, mengambil 500 karakter pertama
    return summarized_text

# Streamlit UI
def main():
    st.title('Ekstraktor dan Pemeringkas Teks URL')
    url_input = st.text_input('Masukkan URL Artikel')
    
    if st.button('Dapatkan Teks'):
        if url_input:
            result_text = get_text_from_url(url_input)
            st.text_area('Teks Artikel', result_text, height=300)
            if st.button('Ringkas Teks'):
                summarized_text = summarize_text(result_text)
                st.text_area('Teks Dirangkum', summarized_text, height=150)
        else:
            st.error('Silakan masukkan URL yang valid.')

if __name__ == "__main__":
    main()
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
if st.button('Lihat Teks'):
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
