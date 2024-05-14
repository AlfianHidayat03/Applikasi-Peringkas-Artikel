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
st.title('Solusi Meringkas Cepat, Tepat, dan Akurat')

# Fungsi untuk mengambil teks dari URL
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join(p.get_text() for p in paragraphs)
    return article_text

# Fungsi untuk meringkas teks
def summarize_text(text):
    try:
        return summarize(text)
    except ValueError:
        return "Teks terlalu pendek untuk diringkas."

def main():
    url_input = st.text_input('Masukkan URL Artikel')
    
    if st.button('Tampilkan Teks'):
        if url_input:
            result_text = get_text_from_url(url_input)
            st.text_area('Teks Artikel', result_text, height=300)
            
            if st.button('Ringkas Teks'):
                summarized_text = summarize_text(result_text)
                st.text_area('Teks Dirangkum', summarized_text, height=150)
        else:
            st.error('Silakan masukkan URL yang valid.')

    uploaded_file = st.file_uploader("Unggah Dokumen (PDF atau DOCX)")
    
    if st.button('Lihat Teks'):
        if uploaded_file:
            if uploaded_file.name.endswith('.pdf'):
                text = read_pdf(uploaded_file)
                st.write(text)
            elif uploaded_file.name.endswith('.docx'):
                text = read_docx(uploaded_file)
                st.write(text)
            else:
                st.error('Format file tidak didukung.')
        else:
            st.error('Silakan unggah file.')

    if st.button('Tampilkan Ringkasan'):
        summary = summarize_text(text)
        st.write(summary)

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

if __name__ == "__main__":
    main()
