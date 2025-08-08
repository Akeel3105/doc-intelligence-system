# ocr_utils.py (improved image handling)
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import fitz
import io

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image):
    image = image.convert("L")  # Grayscale
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    return image

def extract_text_from_image(image):
    image = preprocess_image(image)
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page in doc:
        pix = page.get_pixmap(dpi=300)  # Higher resolution
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        image = preprocess_image(image)
        text += pytesseract.image_to_string(image) + "\n"
    return text
