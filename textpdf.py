import pdfplumber

# Open the PDF file
with pdfplumber.open('example.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"Page {i + 1}:")
        print(text)
