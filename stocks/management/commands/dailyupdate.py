from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock
from stocks.updatehandler import UpdateHandler 
from portfolio.models import Portfolio

class Update_Portfolios(BaseCommand):
	help = "Updates the stock database at the end of the trading day"
	def handle(self, *args, **options):

		



