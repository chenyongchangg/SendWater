"""SendWater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from SendWaterBG import views

urlpatterns = [

    path('admin', admin.site.urls),
    path('creatuser', views.creatUser),
    path('committable', views.commitTable),
    path('getallshop', views.getAllShop),
    path('getoneshop', views.getOneShop),
    path('gethistory', views.getMyHistory),
    path('login', views.login),
    path('addofferman', views.addOfferMan),
    path('addadmin', views.addAdmin),
    path('adminlogin', views.adminLogin),
    path('getmycustomers', views.getMyCustomers),
    path('getallcommittable', views.getAllCommitTable)


]

