# This scrip prepares a dataset for Machine Learning tasks

# Importing packages
import pandas as pd
from TidyColumnNames import TidyColumnNames # TidyColumnNames is a module located in the same directory as the current code

# Reading a randomly generated dataset located in the ..\Miscellaneous directory
df=pd.read_csv(r'..\Miscellaneous\RandomDataset.csv')

# Cleaning the dataset's column names
TidyColumnNames(df)








