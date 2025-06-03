# 🧠 BatikScan API - Klasifikasi Citra Batik Nusantara

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.115.12-green.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-2.19.0-orange.svg)

BatikScan API adalah backend RESTful yang dibangun menggunakan **FastAPI** untuk mengklasifikasikan gambar batik Nusantara menggunakan model machine learning berbasis **TensorFlow**.

---

## 🚀 Fitur

- 🔍 Klasifikasi gambar batik secara otomatis
- 📸 Menerima input gambar format `.jpg`, `.jpeg`, dan `.png`
- 📊 Mengembalikan prediksi kelas dan probabilitas masing-masing kelas
- ⚡ Performa tinggi dengan FastAPI dan Uvicorn
- 🔐 Siap digunakan di server produksi (mis. AWS EC2)

---

## 🧪 Dokumentasi API

📄 Anda bisa melihat dokumentasi API secara interaktif di:
👉 **[http://18.214.158.188:8888/docs](http://18.214.158.188:8888/docs)**  
Dokumentasi ini dibuat otomatis oleh FastAPI menggunakan Swagger UI.

---

## 📦 Instalasi & Menjalankan

### 1. Clone Repo

```bash
git clone https://github.com/username/batikscan-api.git
cd batikscan-api
```

---

## 🖼️ Contoh Respons

```json
{
    "predicted_class": "Yogyakarta_Kawung",
    "confidence": 100.0,
    "probabilities": {
        "JawaBarat_Megamendung": 0.0,
        "Kalimantan_CorakInsang": 0.0,
        "Kalimantan_Dayak": 0.0,
        "Papua_Cendrawasih": 0.0,
        "Solo_Parang": 0.0,
        "Tiongkok_IkatCelup": 0.0,
        "Yogyakarta_Kawung": 100.0
    }
}
```
