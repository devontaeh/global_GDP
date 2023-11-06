import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs =["Bank Name", "MC_USD_Billion"]
csv_path = "E:\Projects\largest_banks\exchange_rate.csv"

def log_progress(message):
    '''Logs message and appends to txt file'''

    format = '%Y-%h-%d-%H:%M:%S'
    time = datetime.now()
    timestamp = time.strftime(format)
    with open("./code_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')

    
def extract(url, table_attribs):
    ''' Extracts required website info and returns dataFrame '''

    response = requests.get(url).text

    #parse HTML
    soup = BeautifulSoup(response, 'html.parser')

    # extract all tbody attribs of HTML and extract all rows
    rows = soup.find_all('table')[0].find_all('tr')
    data_list = []

    for row in rows:
        col = row.find_all('td')
        if col:
            # if col[1].find('a') is not None :   
            data_dict = {"Bank Name": col[1].find_all('a')[1].contents[0], "MC_USD_Billion": float(col[2].contents[0].replace("\n", ""))}
            data_list.append(data_dict)
            
        
    
    df = pd.DataFrame(data_list, columns=table_attribs)
  

    return df


def transform(df, csv_path):
    #Transforms data 
    
    exchange_rate = pd.read_csv(csv_path).set_index('Currency').to_dict()['Rate']
    
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    return df



# def load_to_csv(df, output_path):


# def load_to_db(df, sql_connection, table_name):
    

# def run_query(query_statement, sql_connection):
    


log_progress('Preliminaries complete. Initiating ETL process')

tables = extract(url, table_attribs)
# print(tables)
print(transform(tables,csv_path)['MC_EUR_Billion'][4])


