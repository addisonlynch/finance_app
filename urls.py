from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from stocks import urls as stocks_urls


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(auth_urls)),
    url(r'^accounts/registration/?$',
        'utils.views.registration',
        name='registration'),
    url(r'^', include(stocks_urls)),
)
