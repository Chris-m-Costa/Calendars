from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np




def make_soup(url):
    
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
    else:
        print('failed: ' + request.status_code)
    
    return soup



def scrape_nls(soup):
    
    cln_days = []
    cln_mons = []
    cln_yrs = []
    titles = []
    
    tr = soup.find_all('tr')
    

## For each round item (tr) find date, trim day to race date only (ie 11-13 becomes just 13, fri-sat becomes just sat)
## store dates in clean_dates in format for iCalendar req's
    for i in range(len(soup.find_all('tr'))): 
        temp_date = soup.find_all('tr')[i].find_all('td')[0].text.strip().split('-')[1].split('.')

        temp_day = temp_date[0]
        if temp_day[0] == '0':
            temp_day = temp_day[1:]
        cln_days.append(temp_day)

        temp_mon = temp_date[1]
        if temp_mon[0] == '0':
            temp_mon = temp_mon[1:]
        cln_mons.append(temp_mon)

        cln_yr = temp_date[2]
        cln_yrs.append(cln_yr)

#     clean_dates = []
#     for yr, mon, day in zip(cln_yrs, cln_mons, cln_days):
#         temp_date_ = yr + ', ' + mon + ', ' + day
#         clean_dates.append(temp_date_)
##


## Pull the event names as description and store to description list
    descriptions = []
    for i in range(len(soup.find_all('tr'))):
        temp_desc = soup.find_all('tr')[i].find_all('td')[1].text.strip()
        descriptions.append(temp_desc)
##

## Make a simple title string for each index.
#  index 0 is preseason test days, mnaully added to list
   
    titles = []
    titles.append('NLS Test Days')
    
    count = 1
    for i in range(len(soup.find_all('tr')[1:9])):
        titles.append('NLS Race R0' + str(count))
        count += 1
#         titles.append(temp_tit)
    
    titles.append('NLS Alternative Date')

        
    return cln_yrs, cln_mons, cln_days, descriptions, titles








