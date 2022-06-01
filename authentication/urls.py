"""
All Urls for the authentication app

"""
from django.urls import path

from authentication import views

urlpatterns = [
    # Login API view
    path("user/login", views.UserAuthView.as_view()),
]