# This script generates a random dataset for the purpose of demonstrating data preprocessing tasks

# Importing packages
import pandas as pd
import numpy as np
import random


# Generating columns of the data frame 
# Outcome (y value): Generating an empty list and populating it with 100 values either 0 or 1
outcome_values=[]
for i in range(100):
    if random.random()<=0.05:  # This lines makes sure that 5% of the values are missing values
        value=np.nan
    else:
        value=random.randint(0,1)
    outcome_values.append(value)
# Age: Generating an empty list and populating it with 100 values from 8 to 90
age_values=[]
for i in range(100):
    value=random.randint(8,90)
    age_values.append(value)
# Income: Generating an empty list and populating it with 100 values from 0 to 500,000
income_values=[]
for i in range(100):
    if random.random()<=0.05:  # This lines makes sure that 5% of the values are missing values
        value=np.nan
    else:
        value=random.randint(0,500000)
    income_values.append(value)
# Education Level: Generating an empty list and populating it with 100 values from 1 to 3. 1 represents 'No College Degree', 2 represents 'College Degree', and 3 represents 'Graduate Degree'
education_values=[]
for i in range(100):
    if random.random()<=0.05:  # This lines makes sure that 5% of the values are missing values
        value=np.nan
    else:
        value=random.randint(0,3)
    education_values.append(value)

# Home Ownership: Generating an empty list and populating it with 100 values from the list ['Shelterless','Tenant','Owner']
home_ownership_values=[]
for i in range(100):
    if random.random()<=0.05:  # 5% of values are assumed to be Shelterless
        value='Shelterless'
    elif random.random()<=0.65: # 60% of values are assumed to be Tenant
        value='Tenant'
    else: # The rest are assumed to be 'Owner'
        value='Owner'
    home_ownership_values.append(value)
    
# Relationship Status: Generating an empty list and populating it with 100 values from the list ['Single','Partnered']
relationship_values=[]
Relationship_Categories=['Single','Partnered']
for i in range(100):
    value=random.choice(Relationship_Categories)
    relationship_values.append(value)

# Defining a dictionary with keys as column names and values as column values
# Note that the column names are not tidy; this is pursposeful and they will be fixed in data preprocessing
data = {'_Outcome': outcome_values,
        'Age*':age_values,
        '2020 Annual Income (Dollars)': income_values,
        '   Education':education_values,
        'HOME   OWNERSHIP?  _':home_ownership_values,
        'Relationship/Status   + ':relationship_values}

# Converting the dictionary into a dataframe and saving it as a csv file
df=pd.DataFrame.from_dict(data)
df.to_csv('RandomDataset.csv', index=False)
