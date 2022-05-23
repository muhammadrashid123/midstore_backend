from django.db import models

# Create your models here.

import uuid
from midstore_backend import settings

class Category(models.Model):
    """All Products category will be added in this model"""
    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255, null=False,blank=False)
    image=models.ImageField(upload_to="category_images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_category_uuid = models.UUIDField(null=True, blank=True)
    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.uuid,
                                          self.title,
                                          self.image,
                                          self.parent_category_uuid,
                                          self.created_at,
                                          self.updated_at)


class Products(models.Model):
    """All Products will be added in this model"""

    uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    category = models.ForeignKey(Category,to_field="uuid", on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100,null=False,blank=False)
    image=models.ImageField(upload_to="products_images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0) # stock
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {}".format(self.uuid,
                                               self.category,
                                               self.image,
                                               self.title,
                                               self.price,
                                               self.available_products,
                                               self.created_at,
                                               self.updated_at)
