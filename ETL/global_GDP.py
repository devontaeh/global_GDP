# THIS CODE WILL EXTRACT THE COUNTRY AND THE GDP OF THE LINK

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
CSV_path = './Countries_by_GDP.csv'


def extract(url, table_attribs):
    '''
    extracts website content and saves to dataframe, returns dataframe

    '''

    response = requests.get(url).text

    # parse to HTML

    soup = BeautifulSoup(response, 'html.parser')

    # empty pandas DataFrame
    df = pd.DataFrame(columns=table_attribs)

    # extract all tbody attribs of HTML object -> extract all rows
    rows = soup.find_all('table')[2].find_all('tr')

    # checking all conditions
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:  # row not empty
            # first col has hyperlink and third not empty
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Country": col[0].a.contents[0],  # getting first col and first content
                             "GDP_USD_millions": col[2].contents[0]}  # third col first content
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df, df1], ignore_index=True)

    return df


print(extract(url, table_attribs))
