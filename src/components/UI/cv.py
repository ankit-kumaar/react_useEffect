from docx import Document
from PIL import Image
import pytesseract

# Load the image
image_path = "cvpapa.jpeg"
image = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Create a new Document
doc = Document()

# Add the extracted text to the document
doc.add_paragraph(text)

# Save the document
docx_path = "/desktop/cvPapa.docx"
doc.save(docx_path)

# Return the path of the saved document
docx_path
