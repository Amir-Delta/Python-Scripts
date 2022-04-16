
# Importing packages
import pandas as pd
import numpy as np

# Opening the ASCII file and the associated variable layout
file=open('../Datasets/LLCP2020.ASC','r')
Variable_Layout=pd.read_csv('../Datasets/LLCP2020_Variable_Layout.csv')

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
