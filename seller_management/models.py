from django.db import models
import uuid


class Shop(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    logo = models.ImageField(upload_to='shop_images', null=True)
    shop_type = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField()
    description = models.CharField(max_length=200, null=True, blank=True)