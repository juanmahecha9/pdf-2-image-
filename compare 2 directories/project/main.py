#Imported libraries
import asyncio
import os
import time

#Main project
async def main(path_images, path_pdfs):
    try:
        
        images_files_arr = os.listdir(path_images)
        pdf_paths = os.listdir(path_pdfs)
        pdf_files_arr = []
        for index in range(len(pdf_paths)):
            _path = os.path.join(path_pdfs,pdf_paths[index])
            for file in os.listdir(_path):
                pdf_files_arr.append(file)
        
        #Compare files
        print(str(len(pdf_files_arr)))
        time.sleep(1)
        for file in pdf_files_arr:
            for image in images_files_arr:
                tempF = file.split('.')
                tempI = image.split('.')
                if(tempF[0] == tempI[0]):
                    pdf_files_arr.remove(file)
                
        print(str(len(pdf_files_arr)))
        return "Verify files"
    except Exception as err:
        print(f"Error: {err}")

#Verification of new directory
new_out_path= "C:/Users/mahechacruz.6/BackUP/Rimac/Moving files" #New directory to separate files
images_path= "C:/Users/mahechacruz.6/BackUP/Rimac/Images" #New directory to images

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(images_path, new_out_path))


