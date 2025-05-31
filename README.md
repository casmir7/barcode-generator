This Python script automatically generates 100 barcode images and compiles them into a single PDF. Here’s a breakdown of what it does:

⸻

🔧 Dependencies

You must install:
	•	python-barcode: For generating barcodes
	•	pillow: For image handling
	•	fpdf: For creating PDF documents

⸻

💡 What the Script Does
	1.	Creates a folder named barcodes/
	•	This is where the barcode images will be saved.
	2.	Generates 100 unique barcode values
	•	Format: BARCODE001, BARCODE002, …, BARCODE100
	3.	Creates barcode images
	•	Uses Code128 barcode standard
	•	Each barcode is saved as a .png image in the barcodes/ folder
	4.	Creates a PDF file
	•	Adds a new page for each barcode
	•	Writes the code label (e.g., BARCODE001) above the image
	•	Inserts the corresponding barcode image
	5.	Saves the PDF
	•	The final PDF is named all_barcodes.pdf
	•	Contains 100 pages, each with one barcode

⸻

✅ Output
	•	barcodes/ folder containing 100 .png barcode images
	•	all_barcodes.pdf with 100 pages, each showing one barcode

⸻

📦 Example Use Cases
	•	Product labeling
	•	Inventory tracking
	•	Ticketing systems
	•	Library book tagging
