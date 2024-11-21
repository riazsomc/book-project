from pdf2image import convert_from_path

pages = convert_from_path('CHB.pdf', dpi=300)
for i, page in enumerate(pages):
    page.save(f'page_{i + 1}.jpg', 'JPEG')

import pytesseract
from PIL import Image
import cv2
import numpy as np

image_path = 'page_1.jpg'
image = Image.open(image_path)

def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Denoise the image
    processed_img = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    return processed_img

# Preprocess the image
processed_image = preprocess_image('page_1.jpg')

# Convert to PIL Image for Tesseract
pil_image = Image.fromarray(processed_image)

# Perform OCR on the preprocessed image
text = pytesseract.image_to_string(pil_image, lang='ben', config='--oem 3')

from docx import Document

# Create a new Document
doc = Document()

# Add the extracted text to the document
doc.add_paragraph(text)

# Save the document
doc.save('Extracted_Bangla_Text.docx')

print("Text has been successfully saved to 'Extracted_Bangla_Text.docx'")