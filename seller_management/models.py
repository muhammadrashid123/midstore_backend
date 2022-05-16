from django.db import models

from customer_management.models import User 
import uuid

# Create your models here.
class SellerProfile(models.Model):
    """All Customer will be added in this model"""

    user = models.OneToOneField(User,to_field="uuid", on_delete=models.CASCADE)

class Shop(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    shop_type = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField()
    description = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(SellerProfile, null=True, blank=True, on_delete=models.CASCADE) 