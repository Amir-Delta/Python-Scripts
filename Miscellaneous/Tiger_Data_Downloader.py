# This script downloads 2010 US Census block and 2010 US Census block group TIGER shapefiles for each state from Census website 

# Importing packages
import requests 
import pandas as pd
import numpy as np

# Reading a csv file named states_fips that contains the list of US states and their associated FIPS code
states_fips=pd.read_csv(r"C:\Users\Amir\OneDrive\Independent Projects\Transit Accessibility-EJ\states_fips.csv")

# Writing a for loop that downloads the block and block group shapefiles For each state listed in states_fips and saves them in Data\Blocks and Data\BlockGroups directories
for i in np.arange(len(states_fips)):
    fips=states_fips.loc[i,'fips']
    # Defining urls that point to Tiger shapefiles on Census website
    if fips<10:
        url_block="https://www2.census.gov/geo/tiger/TIGER2010/TABBLOCK/2010/tl_2010_"+"0"+str(fips)+"_tabblock10.zip"
        url_blockgroup="https://www2.census.gov/geo/tiger/TIGER2010/BG/2010/tl_2010_"+"0"+str(fips)+"_bg10.zip"
    else:
        url_block="https://www2.census.gov/geo/tiger/TIGER2010/TABBLOCK/2010/tl_2010_"+str(fips)+"_tabblock10.zip"
        url_blockgroup="https://www2.census.gov/geo/tiger/TIGER2010/BG/2010/tl_2010_"+str(fips)+"_bg10.zip"
    # Downloading the zip files from the urls and saving them in Data folder
    try:
        response=requests.get(url_block)
        file=r"Data\Blocks\block2010_"+str(fips)+".zip"
        open(file,'wb').write(response.content)      
    except Exception:
        pass
    try:
        response=requests.get(url_blockgroup)
        file=r"Data\BlockGroups\blockGroup2010_"+str(fips)+".zip"
        open(file,'wb').write(response.content)      
    except Exception:
        pass


