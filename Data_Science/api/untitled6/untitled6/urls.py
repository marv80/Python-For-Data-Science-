"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path, include
from DevoirALaMaison import views, urls
from django.conf.urls import url


urlpatterns = [
    url('admin/', admin.site.urls),
    url('prediction/', include('DevoirALaMaison.urls'))
]
