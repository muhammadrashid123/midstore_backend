"""
Serializers for seller management

"""


from rest_framework.serializers import ModelSerializer
from seller_management.models import Seller_Shop
from user_profile.serializers import UserProfileReadSerializer


class ShopWriteSerializer(ModelSerializer):
    """Write serializer for the shop, used in create and update shop profile"""

    class Meta:
        model = Seller_Shop
        fields = "__all__"


class ShopReadSerializer(ModelSerializer):
    """Read serializer for the shop user profile, used where user profile needs to be serialized"""
    user = UserProfileReadSerializer(many=False)

    class Meta:
        model = Seller_Shop
        fields = ('uuid', 'name', 'logo', 'shop_type', 'address', 'description', 'user')
# commit