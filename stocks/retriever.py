import pandas_datareader.data as web
from pandas.tseries.offsets import BDay
import pandas as pd
import datetime
from dateutil import rrule
from nyse_date_utils import NYSE_holidays, NYSE_tradingdays, NYSE_trading_calendar


rs = NYSE_trading_calendar()

l1 = list(rs)

l2 = list(rs)

print(l1[1:50])
#print(l2[-1])
exit()
today = pd.datetime.today()
last_month = pd.datetime.today() + datetime.timedelta(-30)
yesterday = pd.datetime.today() - BDay(1)


print(today)
print(last_month)
print(yesterday)

def get_current_data(symbol):
	f = web.DataReader(symbol, 'yahoo', yesterday-BDay(1), today)
	d = f.ix[s]
	print(d)


get_current_data("TSLA")


'''
f = web.DataReader("TSLA", 'yahoo', start, end)
d = f.ix[end]
y = f.ix[start]
change = d['Close'] - y['Close']
PercentChange = float(y['Close']+change)/y['Close']

darr = d.to_dict()
darr.update({"Change" : change})
darr.update({"PercentChange" : PercentChange})
darr.update({"Name" : "blah"})

print(darr)'''