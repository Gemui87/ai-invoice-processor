# 📄 AI-Powered Invoice Intelligence

Sistem ekstraksi data otomatis yang mengubah gambar dokumen (invoice/struk) menjadi data terstruktur menggunakan teknologi Computer Vision dan Large Language Model (LLM).

## 🛠️ Tech Stack
* **Streamlit**: Framework Antarmuka Web.
* **EasyOCR**: Library Vision untuk mendeteksi dan membaca teks dari gambar.
* **Groq Cloud (Llama 3-8B)**: Mesin AI untuk analisis teks mentah menjadi format JSON terstruktur.
* **Python**: Bahasa pemrograman utama.

## 🚀 Fitur Utama
- **OCR Real-time**: Membaca teks dari gambar yang diunggah.
- **AI Analysis**: Mengekstrak nama merchant, tanggal, item barang, dan total harga secara otomatis.
- **Export Ready**: Menghasilkan output dalam format JSON yang siap digunakan untuk integrasi database.

## 📦 Cara Menjalankan
1. Clone repositori ini.
2. Install library: `pip install -r requirements.txt`
3. Masukkan API Key di file `.env`.
4. Jalankan: `streamlit run app.py`