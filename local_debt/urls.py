from django.conf.urls import patterns, include, url
from debt_context import views

urlpatterns = patterns('',
    url(r'^api/search', views.search, name='search'),
    # url(r'^', views.home, name='home'),
)
