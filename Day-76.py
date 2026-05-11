from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir('Files') if file.endswith('.pdf')]

for pdf in files:
    try:
        merger.append(pdf)
    except:                                        #Yaha pa error a raha tha is lia necha wali line ko execute karwana ka lia ya istimal karna pada 
        print(f"Error appending {pdf}.")

# Write the merged PDF to a new file
merger.write("merged-pdf.pdf")
merger.close()