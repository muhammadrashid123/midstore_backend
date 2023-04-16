from django.urls import path
from cart_management import views


urlpatterns = [
    path("cart", views.CartAPIViewset.as_view({'get':'list','post':'create','put':'update','delete':'destroy'})),
    path("checkout", views.CheckoutAPIView.as_view({'post':'create'}))
]
