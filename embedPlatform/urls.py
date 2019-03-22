"""embedPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from embed_nju import process_data
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload_distance', process_data.upload_distance),
    url(r'^upload_temperature', process_data.upload_temperature),
    url(r'^upload_light', process_data.upload_light),
    url(r'^get_data', process_data.get_data),
    url(r'^$', process_data.space)
]
