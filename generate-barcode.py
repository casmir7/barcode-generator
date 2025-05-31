# Install these first if you don't have them:
# pip install python-barcode
# pip install pillow
# pip install fpdf

from barcode import Code128
from barcode.writer import ImageWriter
from fpdf import FPDF
import os

# 1. Prepare a folder to save barcodes
os.makedirs('barcodes', exist_ok=True)

# 2. Create a list of 100 unique codes
codes = [f"BARCODE{i:03d}" for i in range(1, 101)]  # e.g., BARCODE001, BARCODE002, etc.

# 3. Generate barcode images
for code in codes:
    barcode = Code128(code, writer=ImageWriter())
    barcode.save(f"barcodes/{code}")

# 4. Create a PDF and insert all barcodes
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

for code in codes:
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, code, ln=True, align='C')
    pdf.image(f"barcodes/{code}.png", x=30, y=40, w=150)

# 5. Save the PDF
pdf.output("all_barcodes.pdf")

print("PDF with 100 barcodes created successfully!")
