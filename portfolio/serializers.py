from .models import Portfolio
from rest_framework import serializers
from django.contrib.auth.models import User


class PortfolioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Portfolio
		fields = ('user', 'symbol', 'date_created', 'date_modified')