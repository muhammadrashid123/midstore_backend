import uuid
from datetime import datetime
from django.db import models
from rest_framework.authtoken.models import Token
from product_management.models import Products
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Cart(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    product = models.ForeignKey(Products, related_name=("cart_product"), on_delete=models.CASCADE)
    user_token = models.ForeignKey(Token, related_name=("cart_token"), on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self) -> str:
        return super().__str__()
    
class Checkout(models.Model):
    payment_method_choices = (
        ("COD", "Cash On Delivery"),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_products = models.JSONField()
    created_at = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)
    user = models.ForeignKey("user_profile.User", verbose_name=_(""), on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, blank=False)
    payment_method =  models.CharField(max_length=20, choices=payment_method_choices)
    
    def __str__(self):
        return str(self.uuid)