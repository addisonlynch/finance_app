from django.db import models
from django.contrib.auth.models import User

from stocks.models import Stock

# Create your models here.

class Portfolio(models.Model):
	user = models.ForeignKey(User)
	stocks = models.ManyToManyField('stocks.Stock')
	def addStock(self, symbol):
		toadd = Stock.objects.get(symbol=symbol)
		self.stocks.add(toadd)


	def lookupStock(self, symbol):
		query = stocks.objects.filter(Stock__symbol=symbol)
		if query:
			return true
		else:
			return false

	def currentInfo(self):
		querylist = []
		for stock in self.stocks.all():
			query = {
			{'DaysHigh' : stock.DaysHigh },
			{'DaysLow' : stock.DaysLow },
			{'Change' : stock.Change },
			{'PercentChange' : stock.PercentChange },
			{'Symbol' : stock.symbol },
			{'LastTradePriceOnly' : stock.LastTradePriceOnly },
			}
		return querylist
