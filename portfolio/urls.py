from django.conf.urls import *
from .views import *
from rest_framework.urlpatterns import *

urlpatterns = [
    url(r'^$', watch_list, name='watch_list'),
    url(r'^delete_stock/(?P<pk>\d+)/?$', delete_stock, name='delete_stock'),
    url(r'^historical/?$', historical, name='historical'),
    url(r'^plot/?$', plot, name='plot'),
    url(r'^api/portfolio/$', PortfolioAPI.as_view(), name="portfolio api"),
]
