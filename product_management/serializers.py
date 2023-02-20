"""
Serializers for seller management

"""

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from product_management.models import Category, Products


class CategoryWriteSerializer(ModelSerializer):
    """Write serializer for the Category, used in create and update Category details"""

    class Meta:
        model = Category
        fields = "__all__"


class CategoryReadSerializer(ModelSerializer):
    """
    Read serializer for the products' category, used where products category needs to be serialized
    """

    class Meta:
        model = Category
        fields = "__all__"


class ProductsWriteSerializer(ModelSerializer):
    """Write serializer for the products, used in create and update products"""

    class Meta:
        model = Products
        fields = "__all__"


class ProductWriteSerializer(ModelSerializer):
    """Write serializer for the Products, used in create and update Products details"""

    class Meta:
        model = Products
        fields = "__all__"


class ProductsReadSerializer(ModelSerializer):
    """Read serializer for the Products, used where products need to be serialized"""

    # uuid = SerializerMethodField()
    #
    # category = SerializerMethodField()
    #
    # def get_uuid(self, obj):
    #     if obj.uuid:
    #         return str(obj.uuid)
    #
    # def get_category(self, obj):
    #     if obj.category:
    #         return str(obj.category.uuid)

    class Meta:

        model = Products
        fields = "__all__"


class CategoryProductsReadSerializer(ModelSerializer):
    """Read serializer for the category products details, used where products need to be serialized"""
    category = CategoryReadSerializer(many=False)

    class Meta:
        model = Products
        fields = ('uuid', 'title', 'image', 'size', 'color', 'price', 'stock', 'brand_name', 'created_at', 'updated_at',
                  'category')

# class CategoryProductsReadSerializer(ModelSerializer):
#     """Read serializer for the category products details, used where products need to be serialized"""
#     product = ProductsReadSerializer(many=True)
#
#     class Meta:
#         model = Category
#         fields = ('uuid', 'title', 'image', 'created_at', 'updated_at', 'parent_category_uuid',
#                   'product')
