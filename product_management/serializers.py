<<<<<<< Updated upstream
from product_management.models import Category
from rest_framework.serializers import ModelSerializer
from product_management.models import Products
from rest_framework.fields import SerializerMethodField


class CategoryWriteSerializer(ModelSerializer):
    """Write serializer for the products category, used in create and update category"""
=======
"""
Serializers for seller management

"""

from unicodedata import category
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from product_management.models import Category,Product


class CategoryWriteSerializer(ModelSerializer):
    """Write serializer for the shop, used in create and update shop profile"""
>>>>>>> Stashed changes

    class Meta:
        model = Category
        fields = "__all__"


class CategoryReadSerializer(ModelSerializer):
<<<<<<< Updated upstream
    """Read serializer for the products category, used where products category needs to be serialized"""
=======
    """Read serializer for the shop, used where shop needs to be serialized"""

    uuid = SerializerMethodField()

    def get_uuid(self, obj):
        if obj.uuid:
            return str(obj.uuid)
>>>>>>> Stashed changes

    class Meta:
        model = Category
        fields = "__all__"

<<<<<<< Updated upstream

class ProductsWriteSerializer(ModelSerializer):
    """Write serializer for the products, used in create and update products"""

    class Meta:
        model = Products
        fields = "__all__"


class ProductsReadSerializer(ModelSerializer):
    """Read serializer for the products, used where products needs to be serialized"""

    category = SerializerMethodField()

=======
class ProductWriteSerializer(ModelSerializer):
    """Write serializer for the user profile, used in create and update user profile"""

    class Meta:
        model = Product
        fields = "__all__"


class ProductReadSerializer(ModelSerializer):
    """Read serializer for the user profile, used where user profile needs to be serialized"""

    uuid = SerializerMethodField()

    category = SerializerMethodField()

    def get_uuid(self, obj):
        if obj.uuid:
            return str(obj.uuid)

>>>>>>> Stashed changes
    def get_category(self, obj):
        if obj.category:
            return str(obj.category.uuid)

    class Meta:
<<<<<<< Updated upstream
        model = Products
        fields = "__all__"


class CategoryProductsReadSerializer(ModelSerializer):
    """Read serializer for the category products profile, used where products needs to be serialized"""
    category = CategoryReadSerializer(many=False)

    class Meta:
        model = Products
        fields = ('uuid', 'title', 'image', 'price', 'stock', 'brand_name', 'created_at', 'updated_at',
                  'category')
=======
        model = Product
        fields = "__all__"
>>>>>>> Stashed changes
