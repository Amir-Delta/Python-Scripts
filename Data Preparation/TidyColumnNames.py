# This script opens a csv file as a dataframe, and tidies its column names

# Importing packages
import pandas as pd
import re

# Defining functions to transform column names
# 1- Defining a function that lowercases characters. Just as a convention.
def Lowercase(x):
    return x.lower()
# 2- Defining a function that removes Special Characters from a string and replaces them with white spaces. Only alphabets and numbers remain in teh string
def LessSpecialCharacters(x):
    return re.sub('[^A-Za-z0-9]',' ',x)
# 3- Defining a function that removes white space from the beginning and the end of a string, and replaces multiple or single white spaces in the middle of the string with a single underline
def SpaceRemover(x):
    return '_'.join(x.split())
# 4- Defining a function that adds a 'c_' (just as a convention) to the beginning of the string if the first character of the string is a number
def FirstCharacterAString(x):
    if x[0] in ['1','2','3','4','5','6','7','8','9','0']:
        return 'c_'+x
    else:
        return x
    
# Defining a function that takes as input the dataframe and tidies the column names based on previously defined functions
def TidyColumnNames(dataframe):
    col_names=dataframe.columns
    col_names_updated=list(map(Lowercase,col_names))
    col_names_updated=list(map(LessSpecialCharacters,col_names_updated))
    col_names_updated=list(map(SpaceRemover,col_names_updated))
    col_names_updated=list(map(FirstCharacterAString,col_names_updated))
    dataframe.columns=col_names_updated
    return dataframe

 
# Testing the function
# Opening a randomly generated dataframe. The code to create this dataframe is located at ..\Miscellaneous\Random_Dataset_Generator.py
df=pd.read_csv(r'..\Miscellaneous\RandomDataset.csv')

# Tidying dataframe's column names by applying TidyColumnNames function and saving the dataframe as a new csv file
df=TidyColumnNames(df)
df.to_csv(r'..\Miscellaneous\RandomDataset_UpdatedColumnNames.csv', index=False)