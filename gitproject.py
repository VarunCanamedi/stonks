#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import datetime

def total_cases():#function to scrape coronavirus data from www.mohfw.gov.in
    source = requests.get('https://www.mohfw.gov.in/').text
    bat_soup = BeautifulSoup(source,'lxml')
    div = bat_soup.find('div',class_='site-stats-count')
    inf_num = int(div.ul.strong.text)
    return inf_num

t_c=total_cases()

def date_time():#function to get present date and time 
    dates = datetime.datetime.now()
    return dates

date = date_time()
#creating csv file to store data 
with open('corona.csv', 'a+', newline= '') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter = '\t')
    csv_writer.writerow([date, t_c])

