# This script reads data on universities that are ranked in the US News website, cleans them, and saves them in a SQL dataset. 

# Importing libraries
import pandas as pd
import requests
import urllib
from bs4 import BeautifulSoup
import re

#--------------------------------------  Defining some variables/exogenous datasets
# Reading the list of US states as a dataframe. We will use this later for reading associated data from US News website
states=pd.read_csv("csvData.csv")
# Defining headers with a web browser user-agent. Header is used as an argument when getting data from a website. 
# We specify headers with a user-agent of a web browser, because some websites block requests from python or other user-agents. 
headers ={'User-Agent': 'Mozilla/5.0'}


#-------------------------------------- Scraping the website
# Getting HTML data from the US News Best Colleges site and parsing it
main_site=requests.get("https://www.usnews.com/best-colleges/",headers=headers)
main_site_content=main_site.content
main_site_content_soup=BeautifulSoup(main_site_content,"html.parser")
# Getting the link for colleges in each state  and saving it into a new column in the states dataframe.
for i in main_site_content_soup.find_all("a"):
    if i.text in states.State.values:
        states.loc[states.State==i.text,'Website']=i['href']


for i in 
    

_site=requests.get("https://www.usnews.com/best-colleges/api/search?format=json&location=Alabama&_sort=rank&_sortDirection=asc&_page=1",headers=headers)
main_site_content=main_site.content
main_site_content_soup=BeautifulSoup(main_site_content,"html.parser")
for i in main_site_content_soup.find_all("a"):
    print (i)
###############################    

main_site_text=requests.get("https://www.usnews.com/best-colleges/fl",headers=headers).text

# Find the value of total_pages in the above website.
# We need this because there are load_more buttons at the end of each page.  
total_pages = int(re.findall('"total_pages":[0-9]*', main_site_text)[0].split(":")[1])

