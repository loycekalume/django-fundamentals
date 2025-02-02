"""
URL configuration for meeting_planner project.

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
from django.urls import path, include

import django.contrib.auth.urls

from website import views


urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('rooms', views.rooms, name="rooms"),
    path('new', views.new, name="new"),
    path('my_about', views.about),
    path('<int:id>', views.detail,  name="detail"),
    path('edit/<int:id>', views.edit,  name="edit"),
    path('delete/<int:id>', views.delete,  name="delete"),
    path('auth/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
