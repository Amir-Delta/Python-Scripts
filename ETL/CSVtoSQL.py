# This script creates a function that reads a csv file, reads it chunk by chunk, and saves it into a table in a MySQL Database

# Importing the packages
import pandas as pd
from sqlalchemy import create_engine

# Defining the function
def CSVtoSQL(csv_path, chunksize, rdbms, user, password, server, port, database, table):
    engine = create_engine(f'{rdbms}://{user}:{password}@{server}:{port}/') # creating the sqlalchemy engine
    with engine.connect() as conn:
        conn.execute("commit")
        conn.execute(f"CREATE DATABASE IF NOT EXISTS {database}") # creating the database if it does not exist
        conn.close()
    engine = create_engine(f'{rdbms}://{user}:{password}@{server}:{port}/{database}') # creating the sqlalchemy engine to the database
    chunks= pd.read_csv(csv_path, chunksize=chunksize) # reading the csv file chunk by chunk
    for chunk in chunks:
        chunk.to_sql(name=table, con=engine, if_exists = 'append', index=False) # exporting the csv file into the sql database


# Testing the function with a csv file named test_data.csv
if __name__=="__main__":
    CSVtoSQL(csv_path=r'C:\Users\Amir\Downloads\test_data.csv', chunksize=1000,
         rdbms='mysql', user='root', password='root', server='localhost', port=3306, database='here', table='unaveraged'
         )