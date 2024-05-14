# Menggunakan base image Python
FROM python:3.11-slim

# Menyalin file requirements.txt ke container
COPY requirements.txt .

# Menginstal dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Menyalin kode aplikasi ke container
COPY . /app

# Menetapkan direktori kerja
WORKDIR /app

# Menjalankan aplikasi Streamlit
CMD ["streamlit", "run", "peringkas-artikel-streamlit_app.py"]
