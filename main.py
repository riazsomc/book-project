from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import cv2
import numpy as np
from docx import Document
import re

# Preprocessing function
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    processed_img = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)
    return processed_img

def minimal_correction(text):
    """Apply only critical corrections like whitespace before punctuation."""
    # Fix whitespace before Bangla danda (।)
    text = re.sub(r'\s+।', '।', text)
    return text

# Convert PDF to images
pages = convert_from_path('CHB.pdf', dpi=300)
for i, page in enumerate(pages):
    page.save(f'page_{i + 1}.jpg', 'JPEG')

# Create a Word document
doc = Document()

# Perform OCR and correct text
for i in range(len(pages)):
    image_path = f'page_{i + 1}.jpg'
    processed_image = preprocess_image(image_path)
    pil_image = Image.fromarray(processed_image)

    # Extract text
    raw_text = pytesseract.image_to_string(pil_image, lang='ben', config='--oem 3')

    # Apply minimal corrections
    corrected_text = minimal_correction(raw_text)

    # Add to document
    doc.add_paragraph(corrected_text)

# Save the final document
doc.save('Minimal_Corrected_Bangla_Text.docx')

print("Text has been successfully saved to 'Minimal_Corrected_Bangla_Text.docx'")
