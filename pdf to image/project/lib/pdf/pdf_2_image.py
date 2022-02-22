from importlib.resources import path
import shutil
import fitz
from PIL import Image
import os
import time
import shutil

def listFiles2Images(pdf_path, image_path):
    print("Listing files...")
    count = 0
    array = []

    #Open files
    files = os.listdir(pdf_path)
    for file in files:
        count += 1
        if("-page" in file and file.endswith(".pdf")): 
            #print(file)
            splitted = file.split(".")
            image_name = splitted[0] + ".png"
            new_image_path = os.path.join(image_path, image_name)
            file_path = os.path.join(pdf_path, file)
            array.append(new_image_path)
            #Converting files
            convert(file_path, new_image_path, "zip")
            time.sleep(1)
        elif (not file.endswith(".pdf")):
            print("file is not a PDF, this file is moved to the images directory")
            source_path = os.path.join(pdf_path, file)
            shutil.copy(source_path, image_path)
            time.sleep(1)

            
def convert(file_path, out_path, compression):
    try:
        zoom = 2 #To increase the resolution
        mat = fitz.Matrix(zoom,zoom)

        doc = fitz.open(file_path)
        image_list = []
        for page in doc:
            pix = page.get_pixmap(matrix = mat)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            image_list.append(img)

        if image_list:
            image_list[0].save(
                out_path,
                save_all=True,
                append_images=image_list[1:],
                compression=compression,
                dpi=(300, 300),
            )
        
        time.sleep(1)

    except Exception as err:
        print(f"Error converting: {err}")