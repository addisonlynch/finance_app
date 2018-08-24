from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from stocks.views import watch_list 
from utils import views as utils_views

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(auth_urls)),
    url(r'^accounts/registration/?$',
         utils_views.registration,
        name='registration'),
    url(r'^', watch_list),
]
