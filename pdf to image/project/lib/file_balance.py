import os
import math
import asyncio
from lib.verification_directory import verificationDirectory
import shutil


def fileBalance(in_path, number):
    #in_path: path of directory tha contain the pdf files
    #number: number of file for divide 
    try:
        files_list = os.listdir(in_path)
        files_list_count = len(files_list)
        files_quantity = math.ceil(files_list_count/number)
        #New array to store the data
        files_new_array = lambda arr, n: [arr[i:i+n] for i in range(0, len(arr), n)]
        return files_new_array(files_list, files_quantity)
    except Exception as err:
        print(f"Error: {err}")

       
async def movingfiles(array, in_path, out_path):
    #array: array with files to move
    #out_path: new path to copy the files
    try:
        array_length = len(array)
        await asyncio.sleep(0.2)
        count = sum( [ len(listElem) for listElem in array])
        #print(f"Total files to copy: {count}")
        
        directory_array = []

        for index in range(array_length):
            verificationDirectory(out_path+"/Files package "+str(index+1))
            #print(out_path+"/Files package "+str(index+1))
            for file in array[index]:   
                total_items = len(array[index])
                source = in_path + "/" + file
                destination = out_path + "/Files package " + str(index+1)
                #print("Total files in this array: " + str(total_items))
                shutil.copy(source, destination)  
            #Save new directory in the array
            directory_array.append(out_path + "/Files package " + str(index+1))
        return directory_array
    except Exception as err:
        print(f"Error: {err}")

