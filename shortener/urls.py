from django.urls import re_path, path

from shortener.views import UrlExport, UrlShortener, UrlView

urlpatterns = [
    re_path(r'^shortener/(?P<origin_uri>.+)$', UrlShortener.as_view()),
    path('export/', UrlExport.as_view()),
    re_path(r'^(?P<hash>.+)$', UrlView.as_view())
]
