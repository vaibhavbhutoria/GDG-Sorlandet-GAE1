from django.conf.urls import patterns, url
from app1.views import *

urlpatterns = patterns('',
                       url(r'^$', home),
                      )
