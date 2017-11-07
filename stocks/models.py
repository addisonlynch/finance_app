from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from .retriever2 import get_current_info
from jsonfield import JSONField

class Stock(models.Model):
    date_modified = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add=True)


# FROM stock model of IEX
    
    #Cached-values
    symbol = models.CharField(_('Symbol'), max_length=5)
    name = models.CharField(max_length=15)
    primary_exchange = models.CharField(max_length=10)
    sector = models.CharField(max_length=15)

    #Values that are updated daily
    day_volume = models.FloatField()
    previous_close = models.FloatField() #?
    w52_high = models.FloatField()
    w52_low = models.FloatField()
    ytd_change = models.FloatField()

    #Values that are updated intraday
    last_price = models.FloatField(2.0)
    last_volume = models.FloatField()
    day_open = models.FloatField()
    day_close = models.FloatField()
    day_high = models.FloatField()
    day_low = models.FloatField()
    change = models.FloatField()
    percent_change = models.FloatField()
###############################

#groups

   # @property
    def daily(self):
        attributes = {
        "day_volume" : self.day_volume,
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
        return attributes

    #@property
    def intraday(self):
        attributes = {
        "day_open" : self.day_open,
        "day_close": self.day_close,
        "day_high" : self.day_high,
        "day_low"  : self.day_low,
        "change"   : self.change,
        "percent_change" : self.percent_change,
        "last_volume" : self.last_volume,
        "last_price" : self.last_price,
        }
        return attributes




    #@property
    def watch_list(self):
        attributes = {
        "day_open" : self.day_open,
        "day_close": self.day_close,
        "day_high" : self.day_high,
        "day_low"  : self.day_low,
        "change"   : self.change,
        "percent_change" : self.percent_change,
        "day_volume" : self.day_volume,
        }
        return attributes






    def getcurrent(self):
    	pass


