import streamlit as st
import os
import json
import pandas as pd
import numpy as np
from PIL import Image
from dotenv import load_dotenv
from engine.ocr_engine import OCRAgent
from engine.ai_logic import AIAgent

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
load_dotenv()

def safe_format(value):
    try:
        return f"Rp {float(value):,.2f}"
    except (ValueError, TypeError):
        return "Rp 0.00"

@st.cache_resource
def init_agents():
    api_key = os.getenv("GROQ_API_KEY")
    return OCRAgent(), AIAgent(api_key)

ocr_agent, ai_agent = init_agents()

st.set_page_config(page_title="AI Accountant Pro", layout="wide", page_icon="📝")
st.title("AI-Powered Document Intelligence")
st.caption("Audit invoice otomatis dengan pemisahan kontak dan ekstraksi data presisi.")

uploaded_file = st.sidebar.file_uploader("Upload Invoice", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.subheader("Preview Dokumen")
    st.image(image, width=500)
    
    if st.button("Proses Invoice Sekarang", use_container_width=True):
        with st.spinner("AI sedang memproses data..."):
            try:
                text = ocr_agent.extract_text(np.array(image))
                res = ai_agent.analyze_invoice(text)
                data = json.loads(res)
                
                st.divider()
                st.subheader("Hasil Audit Terstruktur")

                h1, h2 = st.columns(2)
                with h1:
                    st.markdown("### Informasi Merchant")
                    m_info = data.get('merchant_info', {})
                    st.info(
                        f"**Nama:** {m_info.get('name', 'N/A')}\n\n"
                        f"**Alamat:** {m_info.get('address', 'N/A')}\n\n"
                        f"**Telp:** {m_info.get('phone', 'N/A')}"
                    )
                with h2:
                    st.markdown("### Informasi Invoice & Customer")
                    inv_info = data.get('invoice_details', {})
                    # Menampilkan Telp dan Email secara terpisah
                    st.success(
                        f"**No Invoice:** {inv_info.get('invoice_number', 'N/A')}\n\n"
                        f"**Tanggal:** {inv_info.get('date', 'N/A')}\n\n"
                        f"**Customer:** {inv_info.get('customer_name', 'N/A')}\n\n"
                        f"**Email:** {inv_info.get('customer_email', 'N/A')}"
                    )

                st.markdown("### Daftar Barang & Jasa")
                df_items = pd.DataFrame(data.get('items', []))
                df_items.columns = [c.replace('_', ' ').title() for c in df_items.columns]
                st.dataframe(df_items, use_container_width=True)

                st.markdown("### Ringkasan Pembayaran")
                sum_data = data.get('summary', {})
                m1, m2, m3, m4 = st.columns(4)
                
                m1.metric("Subtotal", safe_format(sum_data.get('subtotal', 0)))
                
                disc_val = sum_data.get('total_discount', 0)
                m2.metric("Total Diskon", safe_format(disc_val), 
                          delta=f"-{float(disc_val):,.0f}" if float(disc_val) > 0 else None, 
                          delta_color="inverse")
                
                m3.metric("Total Pajak", safe_format(sum_data.get('total_tax', 0)))
                m4.metric("GRAND TOTAL", safe_format(sum_data.get('grand_total', 0)))

                out_bal = sum_data.get('outstanding_balance', 0)
                if out_bal and float(out_bal) > 0:
                    st.warning(f" **Sisa Tagihan (Outstanding):** {safe_format(out_bal)}")

                st.divider()
                csv = df_items.to_csv(index=False).encode('utf-8')
                st.download_button("Download Data ke CSV", data=csv, use_container_width=True, file_name="audit_invoice.csv", mime='text/csv')

            except Exception as e:
                st.error(f"Kesalahan ekstraksi: {e}")