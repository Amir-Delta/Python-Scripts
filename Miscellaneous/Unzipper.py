# This script defines a function that takes as input a path, then reads all the files in that path and unzips those files that have a .zip extension. The unzipped files are saved in the same path.

# Importing packages
import pandas as pd
import numpy as np
import os
from zipfile import ZipFile

# Defining the function
def Unzipper(path):
    # Saving the name of all files in the path in a list called files
    files=os.listdir(path)
    # Defining a for loop that goes through all the files in the path and unzip the zip files (the files with a .zip extension)
    for i in np.arange(len(files)):
        if files[i][-4:]!='.zip':
            continue
        else:
            file_path=path+'\\'+files[i]
            unzipped_name=files[i][:-4] # defining the name of the unzipped file
            try:
                with ZipFile(file_path, 'r') as zipfile:
                   # Extract all the contents of zip file in different directory
                   zipfile.extractall(path+'\\'+unzipped_name)
            except Exception:
                print("The zip file "+files[i]+" cannot be unzipped!")
                pass    

# Testing the function on a path
if __name__=="__main__":
    Unzipper(r"C:\Users\Amir\OneDrive\Independent Projects\Transit Accessibility-EJ\Data\BlockGroups")


   

