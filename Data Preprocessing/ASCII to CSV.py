# This script converts an ASCII file (with fixed column position and lengths) obtained from CDC into a csv one 
# The ASCII file is downloaded from https://www.cdc.gov/brfss/annual_data/2020/files/LLCP2020ASC.zip
# The variable layout of the ASCII file (column positions and lenths) was obtained from https://www.cdc.gov/brfss/annual_data/2020/llcp_varlayout_20_onecolumn.html and saved as a csv file. This file is availeble in "../Miscellaneous"
 
# Importing packages
import pandas as pd
import numpy as np

# Opening the ASCII file and the associated variable layout
file=open('../Datasets/LLCP2020.ASC','r') 
Variable_Layout=pd.read_csv('../Miscellaneous/LLCP2020_Variable_Layout.csv')

# Reading the ASCII file lines, getting the number of rows (lines), and number of columns and column names from variable layout
lines=file.readlines()
nrows=len(lines)
cols=Variable_Layout['Variable Name']
ncols=len(cols)

# Defining an empty dataframe in which we will insert data from the ASCII file. 
df=pd.DataFrame(data=None, index=np.arange(nrows), columns=cols)

# Iterating over the empty dataframe rows and replacing each cell with a value derived from the ASCII file
for index, row in df.iterrows():
    for j in range(ncols):
        start=Variable_Layout.iloc[j,0]
        length=Variable_Layout.iloc[j,2]
        row[j]=lines[index][start-1:start-1+length]

# Saving the dataframe as a csv file
df.to_csv("LLCP2020.csv",header=True,index=False)
