# 📑 AI-Powered Document Intelligence (Invoice Auditor)

Sistem ekstraksi data otomatis yang mengubah gambar dokumen (invoice/struk) menjadi data terstruktur menggunakan teknologi **Computer Vision** dan **Large Language Model (LLM)**. Aplikasi ini dirancang untuk memproses berbagai format invoice secara universal tanpa perlu template kaku.

---

## 🛠️ Tech Stack & Arsitektur
Aplikasi ini dibangun dengan kombinasi teknologi modern yang efisien:

* **Antarmuka Web**: [Streamlit](https://streamlit.io/) - Digunakan untuk membangun dashboard interaktif yang memungkinkan upload dokumen dan visualisasi data secara real-time.
* **Vision Engine (OCR)**: [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Bertindak sebagai "Mata Digital" untuk membaca teks dari gambar. Dikonfigurasi khusus agar berjalan optimal di **CPU**, sehingga hemat resource hardware.
* **AI Reasoning**: [Groq Cloud](https://groq.com/) (**Llama 3.3-70B**) - Bertindak sebagai "Otak Analisis" yang memahami konteks teks, melakukan audit logika, dan mengubah data berantakan menjadi format JSON terstruktur.
* **Pemrosesan Data**: [Pandas](https://pandas.pydata.org/) - Untuk manajemen tabel data dan konversi ke format CSV/Excel.

---

## 🚀 Fitur Unggulan Terbaru
1.  **Universal Invoice Parsing**: Tidak terpaku pada satu desain invoice. AI secara dinamis mencari informasi penting meskipun tata letaknya berbeda-beda.
2.  **Contact Intelligence**: Secara otomatis mendeteksi dan memisahkan informasi **Nomor Telepon** dan **Email** Customer ke dalam kolom yang berbeda.
3.  **Mathematical Audit**: AI melakukan verifikasi perhitungan ($Qty \times Price = Total$) untuk memastikan nomor urut atau teks acak tidak salah terbaca sebagai kuantitas barang.
4.  **Preservasi Format (%)**: Mempertahankan format teks asli untuk kolom Diskon dan Pajak (seperti menampilkan "10%" atau "PPN 11%") sesuai dokumen asli.
5.  **Robust Error Handling**: Dilengkapi dengan fungsi *safe formatting* untuk mencegah aplikasi crash jika terdapat data yang kosong atau tidak terbaca.

---

## 🔄 Alur Kerja Sistem (Workflow)
1.  **Upload**: User mengunggah gambar (JPG/PNG) melalui dashboard Streamlit.
2.  **Extract**: EasyOCR memindai gambar dan menghasilkan teks mentah (*raw text*).
3.  **Analyze**: Teks mentah dikirim ke Llama 3.3 via Groq. AI melakukan pembersihan data, klasifikasi entitas, dan pengecekan logika matematika.
4.  **Visualize**: Data yang sudah rapi ditampilkan dalam tabel interaktif dan metrik ringkasan pembayaran.
5.  **Export**: Data siap diunduh dalam format CSV untuk kebutuhan pembukuan lebih lanjut.

---

## 📦 Cara Menjalankan di Lokal

1.  **Clone Repositori**:
    ```bash
    git clone [https://github.com/Gemui87/ai-invoice-processor.git](https://github.com/Gemui87/ai-invoice-processor.git)
    cd ai-invoice-processor
    ```

2.  **Instalasi Library**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Konfigurasi API Key**:
    Buat file `.env` di folder utama dan masukkan API Key Groq Anda:
    ```env
    GROQ_API_KEY=your_api_key_here
    ```

4.  **Jalankan Aplikasi**:
    ```bash
    streamlit run app.py
    ```

---

## 🛡️ Keamanan Data
Proyek ini menggunakan `.gitignore` untuk memastikan file sensitif seperti `.env` tidak terunggah ke repositori publik, menjaga kerahasiaan API Key pengguna.
