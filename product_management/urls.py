from django.urls import path
from product_management import views


urlpatterns = [

    # product CRUD view
    path("category", views.CategoryView.as_view()),
    path("product", views.ProductsView.as_view()),
]