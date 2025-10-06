import pytesseract
from PIL import Image

def extract_text_from_images(image_paths):
    text_output = []
    for img_path in image_paths:
        text = pytesseract.image_to_string(Image.open(img_path))
        text_output.append({"image": img_path, "text": text.strip()})
    return text_output
