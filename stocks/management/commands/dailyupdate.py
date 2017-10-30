from django.core.management.base import BaseCommand, CommandError
from stocks.models import Stock
class Command(BaseCommand):
	help = "Updates the stock database at the end of the trading day"
	def handle(self, *args, **options):
		print("hello world!")



