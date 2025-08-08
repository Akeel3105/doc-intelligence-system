# app.py
import streamlit as st
from PIL import Image
import pytesseract
import fitz  # PyMuPDF for PDF reading
import io
from ocr_utils import extract_text_from_image, extract_text_from_pdf
from nlp_utils import extract_entities
from logger import save_to_csv

st.set_page_config(page_title="Document Intelligence System", layout="wide")

st.title("🧾 Real-Time Document Intelligence (OCR + NLP)_Updated")
st.write("Upload a scanned image or PDF to extract structured information.")

uploaded_file = st.file_uploader("Upload Document (PDF or Image)", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_fil:
    file_bytes = uploaded_file.read()
    text = ""

    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(file_bytes)
    else:
        image = Image.open(io.BytesIO(file_bytes))
        text = extract_text_from_image(image)

    st.subheader("📜 Extracted Text")
    st.text_area("Raw OCR Output", text, height=200)

    if text:
        st.subheader("🔍 Extracted Fields")
        results = extract_entities(text)
        st.json(results)

        if st.button("✅ Save Log"):
            save_to_csv(results)
            st.success("Saved successfully!")
