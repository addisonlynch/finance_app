from stocks.models import Stock
from iexretriever import IEXRetriever as iex 

from .models import Portfolio



iex_attributes = {

        "day_volume" : "day_volume",
        "previous_close" : self.previous_close,
        "w52_high" : self.w52_high,
        "w52_low"  : self.w52_low,
        "ytd_change" : self.ytd_change,
        "day_open" : self.day_open,
        "day_close": self.day_close,
        "day_high" : self.day_high,
        "day_low"  : self.day_low,
        "change"   : self.change,
        "percent_change" : self.percent_change,
        "last_volume" : self.last_volume,
        "last_price" : self.last_price,
}


class UpdateHandler(object):

	def __init__(self):
		pass

	def Update_Portfolio_Daily(self):
		pass


	def Update_Watchlist_Intraday(self):
		pass

