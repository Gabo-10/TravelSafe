"""
URL configuration for APIGABO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home
from api.views import Inicio
from api.views import power
from api import views
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.registro ,name='form'),
    path('', views.inicio_de_sesion ,name='login'),
    # path('edit/', views.editar ,name='edit'),
    path('index/',Inicio.as_view(),name='index'),
    path('dashboard/',power.as_view(),name='dash')
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
urlpatterns += staticfiles_urlpatterns() # new