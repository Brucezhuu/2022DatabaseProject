"""mysite URL Configuration

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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('user/list', views.user_list),
    path('login/student/', views.StudentLogin),
    path('register/student/', views.StudentRegister),
    path('login/teacher/', views.TeacherLogin),
    path('register/teacher', views.TeacherRegister),
    path('update/pwd/student', views.update_pwd_student),
    path('update/pwd/teacher', views.update_pwd_teacher),
]
