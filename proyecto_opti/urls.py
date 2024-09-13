"""
URL configuration for proyecto_opti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from no_lineal import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dorada/', views.seccion_dorada, name='seccion_dorada'),
    path('', views.multiplicadores, name='multiplicadores'),
    path('gradiente/', views.gradiente, name='gradiente'),
    path('cuadratica/', views.cuadratica, name='cuadratica'),
    path('combinaciones_lineales/', views.combinaciones_lineales, name='combinaciones_lineales'),
    path('programacion_estocastica/', views.programacion_estocastica, name='programacion_estocastica'),
    path('programacion_separable/', views.programacion_separable, name='programacion_separable'),
    path('sumt/', views.sumt, name='sumt'),
]
