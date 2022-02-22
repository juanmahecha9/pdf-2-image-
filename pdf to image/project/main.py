#Import libs
from lib.verification_directory import verificationDirectory
from lib.file_balance import fileBalance, movingfiles
import asyncio
from lib.pdf.pdf_split import pdf2sheets
from lib.pdf.pdf_2_image import listFiles2Images
import time
import os

#Main project
async def main(files_path, new_out_path,images_path):
    verificationDirectory(new_out_path)
    verificationDirectory(images_path)
    files_array = fileBalance(files_path,10)
    new_directories = await movingfiles(files_array, files_path, new_out_path)
    #print(new_directories)
    for path in new_directories:
        pdf2sheets(path)
    time.sleep(0.5)
    for path in new_directories:
        listFiles2Images(path, images_path)

#Verification of new directory
files_path = "C:/Users/mahechacruz.6/BackUP/Rimac/Segundo envío de archivos"
new_out_path= "C:/Users/mahechacruz.6/BackUP/Rimac/Moving files" #New directory to separate files
images_path= "C:/Users/mahechacruz.6/BackUP/Rimac/Images" #New directory to images

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(files_path, new_out_path,images_path))


