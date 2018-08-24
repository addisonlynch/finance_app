import pandas_datareader.data as web
from pandas.tseries.offsets import BDay
import pandas as pd
import datetime
from dateutil import rrule

import requests


#from nyse_date_utils import NYSE_holidays, NYSE_tradingdays, populate_list

#from stocks.models import Stock 

today = datetime.date.today() + datetime.timedelta(-1)
last_month = datetime.date.today() + datetime.timedelta(-30)
yesterday = datetime.date.today() + datetime.timedelta(-2)
last_year = datetime.date.today() + datetime.timedelta(-365)

todaysend = today #str(today.strftime('%Y-%m-%d'))
yesterdaysend = yesterday#str(yesterday.strftime('%Y-%m-%d'))
def get_all_data(symbol):
	pass
	#f = web.DataReader(symbol, 'yahoo', last_year, today)
	#d = f.ix[today]
	#print(d)

def get_last(symbol):
	return web.get_quote_yahoo(symbol).iloc[0]['last']

def get_current_info(symbols):
	retval = []
	for symbol in symbols:
		g = web.DataReader(symbol, 'yahoo', yesterdaysend, todaysend)
		f = g.round(2)
		f.index = pd.to_datetime(f.index)
		print(f)
		d = f.ix[todaysend]
		y = f.ix[yesterdaysend]
		change = d['Close'] - y['Close']
		PercentChange = (y['Close']/(y['Close']+change))
		darr = d.to_dict()
		darr['DaysHigh'] = darr.pop('High')
		darr['DaysLow'] = darr.pop('Low')
		darr.update({"Change" : change})
		darr.update({"PercentChange" : round(PercentChange,2)})
		darr.update({"Name" : "Junk"})
		darr.update({"Symbol" : symbol})
		darr.update({"LastTradePriceOnly" : get_last(symbol)})
		print(darr)
		retval.append(darr)
	return (retval)

def get_historical_info(symbol):
	pass

def get_month_info(symbol):
	pass 



'''

print(darr)'''