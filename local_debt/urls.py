from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from debt_context import views

urlpatterns = patterns(
    '',
    url(r'^api/search', views.search, name='search'),
    url(r'^', TemplateView.as_view(template_name='index.html'), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
