from groq import Groq

class AIAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def analyze_invoice(self, raw_text):
        prompt = f"""
        Teks OCR: {raw_text}
        
        Tugas: Ekstrak data invoice secara UNIVERSAL ke format JSON.
        
        LOGIKA EKSTRAKSI:
        1. **Merchant**: Ambil nama perusahaan, alamat, dan nomor telepon pengirim.
        2. **Customer**: Cari setelah kata kunci 'Tagihan Kepada', 'Bill To', atau 'Kepada'.
           - Pisahkan 'phone' dan 'email' menjadi field yang berbeda.
        3. **Items**: Identifikasi baris tabel. 
           - Gunakan logika matematika (Qty * Unit Price) untuk menentukan Qty yang benar.
           - Abaikan nomor urut di awal baris.
           - Untuk 'discount' dan 'tax', ambil teks asli (misal: "10%", "PPN 10%").
        4. **Summary**: Jika nilai numerik tidak ditemukan, berikan angka 0 (jangan None).

        Format JSON:
        {{
          "merchant_info": {{ "name": "N/A", "address": "N/A", "phone": "N/A" }},
          "invoice_details": {{
            "date": "YYYY-MM-DD",
            "invoice_number": "N/A",
            "customer_name": "N/A",
            "customer_phone": "N/A",
            "customer_email": "N/A",
            "customer_address": "N/A"
          }},
          "items": [
            {{
              "name": "N/A",
              "qty": 0,
              "unit_price": 0,
              "discount": "0",
              "tax": "0",
              "line_total": 0
            }}
          ],
          "summary": {{
            "subtotal": 0,
            "total_discount": 0,
            "total_tax": 0,
            "grand_total": 0,
            "outstanding_balance": 0
          }}
        }}
        """
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a universal invoice auditor. Always split phone and email into separate fields. Return 0 for missing numbers."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile", 
            response_format={"type": "json_object"}
        )
        return chat_completion.choices[0].message.content