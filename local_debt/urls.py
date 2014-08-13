from django.conf.urls import patterns, include, url
from debt_compare import views

urlpatterns = patterns('',
    url(r'^api/', views.index, name='index')
)
