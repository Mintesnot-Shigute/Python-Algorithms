from reportlab.pdfgen import canvas
from PIL import Image

def convert_image_to_pdf(image_path, pdf_path):
    # Open the image file
    img = Image.open(image_path)

    # Get image dimensions
    width, height = img.size

    # Create a PDF file
    pdf = canvas.Canvas(pdf_path, pagesize=(width, height))

    # Draw the image on the PDF
    pdf.drawImage(image_path, 0, 0, width, height)

    # Save the PDF file
    pdf.save()

# Example usage
image_path = r"C:\Users\MintesnotS\Documents\MY IMAGE.jpg"
pdf_path = r"C:\Users\MintesnotS\Documents\output.pdf"
# Replace with the desired output PDF file path

convert_image_to_pdf(image_path, pdf_path)
