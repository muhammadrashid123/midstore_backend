"""
model for product Management
"""
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    """
    All Products' category will be added in this model
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to="category_images", null=True)
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
    """
    All Products will be added in this model
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, to_field="uuid", on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="products_images", null=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    brand_name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.uuid,
                                                                             self.category.title,
                                                                             self.image,
                                                                             self.title,
                                                                             self.size,
                                                                             self.color,
                                                                             self.price,
                                                                             self.stock,
                                                                             self.brand_name,
                                                                             self.created_at,
                                                                             self.updated_at)

# from unicodedata import category
# from django.db import models
# import uuid
#
# # Create your models here.
#
# # Product Category -> Image & Name
# class Category(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=200, null=False, blank=False)
#     image = models.ImageField(upload_to='category_images', null=True)
#
# # Product -> Name, Price, Description, Size, Color, Quantity, Exchange_product, Image
# class Product(models.Model):
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=200, null=False, blank=False)
#     price = models.IntegerField(null=False, blank=False)
#     description = models.CharField(max_length=200, null=False, blank=False)
#     size = models.CharField(null=False, blank=False)
#     color = models.CharField(max_length=200, null=False, blank=False)
#     quantity = models.IntegerField(null=False, blank=False)
#     exchange_product = models.CharField(max_length=200, null=True, blank=True)
#     image = models.ImageField(upload_to='product_images', null=True)
#     category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
