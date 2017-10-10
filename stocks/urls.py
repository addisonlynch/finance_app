from django.conf.urls import *
from stocks.views import *


urlpatterns = [
    url(r'^$', portfolio, name='portfolio'),
    url(r'^delete_stock/(?P<pk>\d+)/?$', delete_stock, name='delete_stock'),
    url(r'^historical/?$', historical, name='historical'),
    url(r'^plot/?$', plot, name='plot'),
]
