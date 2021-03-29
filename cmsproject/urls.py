"""cmsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cmsapp.views import home, showdept, adddept, deletedept, showstudent, addstudent, deletestudent, showsport, addsport, deletesport, showinfo, addinfo, deleteinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('showdept/',showdept, name='showdept'),
    path('adddept/',adddept, name='adddept'),
    path('deletedept/<int:id>',deletedept,name="deletedept"),
    path('showstudent',showstudent,name="showstudent"),
    path('addstudent',addstudent, name='addstudent'),
    path('deletestudent/<int:id>',deletestudent,name='deletestudent'),
    path('showsport',showsport,name="showsport"),
    path('addsport',addsport, name='addsport'),
    path('deletesport/<int:id>',deletesport,name='deletesport'),
    path('showinfo',showinfo,name="showinfo"),
    path('addinfo',addinfo, name='addinfo'),
    path('deleteinfo/<int:id>',deleteinfo,name='deleteinfo'),
]
