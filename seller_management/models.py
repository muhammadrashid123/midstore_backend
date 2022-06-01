from django.db import models
import uuid

from user_profile.models import User


class Seller_Shop(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    logo = models.ImageField(upload_to='shop_images', null=True)
    shop_type = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)