try: import simplejson as json
except ImportError: import json
import xlwt
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import StockSerializer
from .models import Stock



class LastPrice(generics.ListCreateAPIView):
    model = Stock
    serializer_class = StockSerializer
    def get_queryset(self):
        queryset = Stock.objects.all()
        sym = self.kwargs['sym']
        queryset = queryset.filter(symbol=sym)
        return queryset 
    def perform_create(self, serializer):
        serializer.save()
