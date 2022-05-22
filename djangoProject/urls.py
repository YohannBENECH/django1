"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from lycee import views

handler404 = 'lycee.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lycee', views.index, name='index'),

    #path('lycee/<int:cursus_id>', views.detail, name='detail'),
    path('lycee/<int:cursusId>', views.ClassView, name='ClassView'),
    path('lycee/cursuscall/<int:cursusId>', views.callRollClassroomView, name='callRollClassroomView'),
    path('lycee/students/<int:studentId>', views.studentView, name='studentView'),
    path('lycee/students/create', views.createStudentForm, name='createStudentForm'),
    path('lycee/students/edit/<int:studentId>', views.editStudentForm, name='editStudentForm'),
    path('lycee/call', views.callOfRoll, name='callOfRoll')
]

