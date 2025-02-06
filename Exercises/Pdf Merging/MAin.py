from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith('.pdf')]
for file in files:
    merger.append(file)

merger.write('Merged.pdf')
merger.close()


