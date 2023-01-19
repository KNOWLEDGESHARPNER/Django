"""DatabaseProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from student import views

urlpatterns = [
   path('',views.home),
   path('reg',views.f1,name='reg'),
   path('log',views.f2,name='log'),
   path('logout',views.f4,name='logout'),
   path('show',views.f3,name='show'),
   path('registration',views.registrationfunction),
   path('loginaction',views.loginaction),
   path('update/<int:id>',views.updatefunction,name='update'),
   path('delete/<int:id>',views.deletefunction,name='delete'),

]
