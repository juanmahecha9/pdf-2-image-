import os
from threading import local
from PyPDF2 import PdfFileReader, PdfFileWriter
import time

def pdf2sheets(pdf_path):
    try:
        #(pdf_path)
        files= os.listdir(pdf_path)
        count_page = 1
        for file in files:
            if ".pdf" in file:
                time.sleep(1)

                name = file.replace(".pdf","")
                
                #Read PDF file
                file_path = pdf_path+ "/" + file
                pdfReader = PdfFileReader(open(file_path, "rb"))
                count_pages = pdfReader.getNumPages()
                
                #Count pages
                container = {}
                
                for page in range(count_pages):
                    container[f"pdf_writer{page}"] = PdfFileWriter()
                    container[f"pdf_writer{page}"].addPage(pdfReader.getPage(page))
                   
                    with open(f"{pdf_path}/{name}-page-{page}.pdf","wb") as doc_file:
                       container[f"pdf_writer{page}"].write(doc_file)
                    time.sleep(1)

            else: 
                print("No es pdf")

    except Exception as e:
        print (f"Error")


