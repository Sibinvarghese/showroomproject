
from django.contrib import admin
from django.urls import path
from user.views import UserHomePage
urlpatterns = [
    path("userhomepage",UserHomePage.as_view(),name="userhome"),
]

