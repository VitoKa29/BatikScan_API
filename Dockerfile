# Gunakan Python image yang kompatibel
FROM python:3.10

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Buat dan pindah ke direktori kerja
WORKDIR /app

# Salin file requirements dan install dependensi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke container
COPY . .

# Jalankan aplikasi
CMD ["python", "main.py"]
