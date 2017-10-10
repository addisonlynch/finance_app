from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from stocks import urls as stocks_urls
from utils import views as utils_views

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(auth_urls)),
    url(r'^accounts/registration/?$',
         utils_views.registration,
        name='registration'),
    url(r'^', include(stocks_urls)),
]
