"""
All urls for the seller management app
"""

from django.urls import path
from seller_management import views

urlpatterns = [
  # Shop CRUD view
  path("shop", views.ShopView.as_view())

]