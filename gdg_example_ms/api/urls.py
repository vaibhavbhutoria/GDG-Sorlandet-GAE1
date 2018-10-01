from django.conf.urls import patterns, url
from api.views import *
urlpatterns = patterns('',
                       url(r'^usd-to-nok/',usd_to_nok)
                      )
