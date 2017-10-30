from django.conf.urls import *
from .views import *
from rest_framework.urlpatterns import *

urlpatterns = [
    url(r'^api/now/(?P<sym>\w+)$', LastPrice.as_view(), name="last price")
]
