def test_dummy():
    assert True

def extract_text_from_image(image_path):
    # implementation
    return "PAN Number: ABCDE1234F"

from utils.ocr_utils import extract_text_from_image

def test_ocr_extraction():
    result = extract_text_from_image("tests/sample_pan.jpg")
    assert "PAN" in result

