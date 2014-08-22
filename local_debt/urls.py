from django.conf.urls import patterns, include, url
from debt_context import views

urlpatterns = patterns('',
    url(r'^api/location', views.location, name='location'),
    url(r'^api/search', views.search, name='search'),
)
