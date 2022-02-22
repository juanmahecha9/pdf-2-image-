import os
import time

def verificationDirectory(path):
    try:
        print (f"Verifying directory {path} in process...")
        time.sleep(1)
        if os.path.exists(path):
           os.remove(path)
           time.sleep(0.2)
           os.mkdir(path)
        else:
           os.mkdir(path)
    except Exception as e:
        print(f"Error: {e}")