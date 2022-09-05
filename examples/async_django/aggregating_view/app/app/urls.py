"""app URL Configuration

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
from django.urls import path

import app.views as views

urlpatterns = [
    path("hotels/<int:pk>/", views.HotelDetail.as_view(), name="hotel-detail"),
    path("rooms/", views.RoomList.as_view(), name="room-list"),
    path("hotels/<int:pk>/rooms/", views.HotelRooms.as_view(), name="hotel-rooms"),
]
