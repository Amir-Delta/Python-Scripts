# This script scrapes data on ranked colleges from the US News website, cleans the data and saves it in a SQL dataset. 

# Importing libraries
import requests
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import json

# Defining headers with a web browser user-agent. Header is used as an argument when getting data from a website. 
# We specify headers with a user-agent of a web browser, because some websites block requests from python or other user-agents. 
headers ={'User-Agent': 'Mozilla/5.0'}

# ------------------------Creating a list of all ranked colleges in US NEWS and their associated US NEWS website----------------------

# Specifying the link to best colleges search API
LINK = "https://www.usnews.com/best-colleges/api/search?format=json&schoolType=national-universities&_sort=rank&_sortDirection=asc&_page=1"
# To find this link, go to inspect elements of the https://www.usnews.com/best-colleges/rankings/national-universities website in a...
# ...browser, then to Network tab, filter by XHR, and scroll down the website till more search results are loaded and the link is...
# ... appeared in the inspect section.

# Defining a function that use the state's college serch API to get search data as json
def get_data(url):
    response = requests.get(url, headers=headers)
    data = response.json()["data"]
    return data["items"], data["next_link"] # The next page in the colleges search API
# Using the above function to get search data in the first page of search and also the link for the next page of search results
items, next_link = get_data(LINK)

# Scraping data from all the pages of the search results untill there is no more page left. 
while next_link is not None:
    new_items, next_link = get_data(next_link)
    items += new_items

# Defining a dictionary with the list of college names and their associated US NEWS website
colleges_dict = [
        {"name": item["institution"]["displayName"],
         "link": "https://www.usnews.com"+re.findall('href=".*"', item['institution']['linkedDisplayName'])[0].split('"')[1]}
        for item in items]
# Converting the dictionary into a dataframe
colleges = pd.DataFrame(colleges_dict)

# Adding columns to colleges dataframe with no values. The values will be updated later in the code. 
colleges['sch_type']=np.nan
colleges['year_found']=np.nan
colleges['relif_affil']=np.nan
colleges['acad_calend']=np.nan
colleges['sch_setting']=np.nan
colleges['rank_22']=np.nan


# ------------------------ Scraping data for each college----------------------

# Defining a for loop that goes to each college's link on US News website and scrapes its information
for row in np.arange(len(colleges)):
    link=colleges.loc[row]['link']
    link_text=requests.get(link,headers=headers).text
    colleges.loc[row,['sch_type']]=re.sub('"','',re.findall('"displayValue":(.*)',re.findall('"label":"school type",(.*?)}',link_text)[0])[0])
    colleges.loc[row,['year_found']]=re.sub('"','',re.findall('"displayValue":(.*)',re.findall('"label":"year founded",(.*?)}',link_text)[0])[0])
    colleges.loc[row,['relif_affil']]=re.sub('"','',re.findall('"displayValue":(.*)',re.findall('"label":"religious affiliation",(.*?)}',link_text)[0])[0])
    colleges.loc[row,['acad_calend']]=re.sub('"','',re.findall('"displayValue":(.*)',re.findall('"label":"academic calendar",(.*?)}',link_text)[0])[0])
    colleges.loc[row,['sch_setting']]=re.sub('"','',re.findall('"displayValue":(.*)',re.findall('"label":"setting",(.*?)}',link_text)[0])[0])
    ranking_link=link+"/overall-rankings"
    ranking_link_text=requests.get(ranking_link,headers=headers).text
    try:
        colleges.loc[row,['rank_22']]=re.findall('ranked #(.*?) in National Universities',ranking_link_text)[0]
    except:
        pass









