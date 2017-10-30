import sys, http.client
import urllib.parse
try: import simplejson as json
except ImportError: import json

import pandas as pd
import requests
import logging
logging.basicConfig(level=logging.DEBUG)
import datetime

from pandas.tseries.offsets import BDay


today = datetime.date.today() + datetime.timedelta(-1)
last_month = datetime.date.today() + datetime.timedelta(-30)
yesterday = pd.datetime.today() + BDay(-1)
last_year = datetime.date.today() + datetime.timedelta(-365)
five_ago = today - datetime.timedelta(-5)



indicies={

	 "nyse" : "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download" ,
	 "nasdaq" : "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download" ,
	 "amex" : "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download" ,
}

functions={
	"intraday" : "TIME_SERIES_INTRADAY",
	"daily"	   : "TIME_SERIES_DAILY",
	"dailyadj" : "TIME_SERIES_DAILY_ADJUSTED",
}

PUBLIC_API_URL = 'https://www.alphavantage.co/query'
API_KEY = 'LKJIW85X3DC96E4M'

def executeAVQuery(queryfields):
	querystring = urllib.parse.urlencode(queryfields)
	url = (PUBLIC_API_URL + '?' + querystring + '&apikey=' + API_KEY)
	print(url)
	r = requests.get(url=url)
	return r.json()



class AVQueryError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def functionHandler():
	pass

def get_current_info(symbolList, columnsToRetrieve='*'):
    """Retrieves the latest data (15 minute delay) for the 
    provided symbols."""
    columns = ','.join(columnsToRetrieve)
    i = 0
    f = {}
    for symbol in get_index_symbol_list("nyse"):
    	f["symbol"] = symbol
    f["function"] = functions["intraday"]
    response = executeAVQuery(yql)
    return __validate_response(response, 'quote')


def get_index_symbol_list(index):
	df = pd.DataFrame.from_csv(indicies[index])
	return df.index.tolist()


if __name__ == "__main__":
	x = executeAVQuery({'symbol' : 'TSLA', 'function' : functions["daily"]})
	u = x[u'Time Series (Daily)'][yesterday.strftime('%Y-%m-%d')]
	print(u)

	exit()

