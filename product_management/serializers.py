from product_management.models import Category
from rest_framework import serializers
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from product_management.models import Products
from rest_framework.fields import SerializerMethodField


class CategoryWriteSerializer(ModelSerializer):
    """Write serializer for the products category, used in create and update category"""

    class Meta:
        model=Category
        fields = "__all__"


class CategoryReadSerializer(ModelSerializer):
    """Read serializer for the products category, used where products category needs to be serialized"""

    class Meta:
        model=Category
        fields = "__all__"



class ProductsWriteSerializer(ModelSerializer):
    """Write serializer for the products, used in create and update products"""

    class Meta:
        model=Products
        fields = "__all__"



class ProductsReadSerializer(ModelSerializer):
    """Read serializer for the products, used where products needs to be serialized"""

    category=SerializerMethodField()


    def get_category(self,obj):
        if obj.category:
            return str(obj.category.uuid)



    class Meta:
        model=Products
        fields="__all__"

class CategoryProductsReadSerializer(ModelSerializer):
    """Read serializer for the category products profile, used where products needs to be serialized"""
    class Meta:
        model = Products
        exclude = ('category', )
