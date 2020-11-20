from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shortener.views import UrlListViewSet

router = routers.SimpleRouter()
router.register('', UrlListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls'))
]

urlpatterns += router.urls