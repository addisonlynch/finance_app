from rest_framework import serializers
from .models import Stock
from django.contrib.auth.models import User

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		fields = ('symbol', 'lastprice')


