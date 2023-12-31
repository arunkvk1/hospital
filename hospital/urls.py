"""
URL configuration for hospital project.

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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("admin1/",views.admin1),
    path('pat/',views.patient),
    path("adddoctor/",views.adddoctor),
    path("doct/",views.doct),
    path("viewdoctor/",views.viewdoctor),
    path('deletedoctor/<int:id>',views.deletedoctor),
    path('addpatient/',views.addpatient),
    path('link1/',views.link1),
    path('viewdoctor1/',views.viewdoctor1),
    path('viewpro/',views.viewprofile),
    path('updatepro/<int:id>',views.updateprofile),
    path('link2/<int:id>',views.link2),
    path('deletepro/<int:id>',views.deleteprofile)
    
]
