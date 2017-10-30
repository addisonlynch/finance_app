from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from .retriever import get_current_info


class Stock(models.Model):
    symbol = models.CharField(_('Symbol'), max_length=5)
    date_modified = models.DateTimeField(auto_now = True)
    date_created = models.DateTimeField(auto_now_add=True)
    lastprice = models.FloatField(2.0)
    DaysHigh = models.FloatField()
    DaysLow = models.FloatField()
    Change = models.FloatField()
    PercentChange = models.FloatField()
    LastTradePriceOnly = models.FloatField()

    def getcurrent(self):
    	return get_current_info(self.symbol)


