"""
URL configuration for disease_predict project.

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
from predict.views import home,parkinson,heart,diabetes,printHistory,result,not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('result/',result,name='result'),
    path('parkinson/',parkinson,name='parkinson'),
    path('heart/',heart,name='heart'),
    path('diabetes/',diabetes,name='diabetes'),
    path('history/',printHistory,name='history'),
    path('<str:unknown_path>',not_found,name='error')


]
