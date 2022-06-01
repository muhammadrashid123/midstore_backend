"""
Serializers for the user profile app

"""


from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from user_profile.models import Cart, DeliveryCost, User


class UserProfileWriteSerializer(ModelSerializer):
    """Write serializer for the user profile, used in create and update user profile"""

    class Meta:
        model = User
        fields = "__all__"


class UserProfileReadSerializer(ModelSerializer):
    """Read serializer for the user profile, used where user profile needs to be serialized"""

    # uuid = SerializerMethodField()
    #
    # shop = SerializerMethodField()

    # def get_uuid(self, obj):
    #     if obj.uuid:
    #         return str(obj.uuid)
    #
    # def get_shop(self, obj):
    #     if obj.shop:
    #         return str(obj.shop.uuid)

    class Meta:
        model = User
        fields = "__all__"

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item', 'quantity', 'created_at', 'updated_at']


class DeliveryCostSerializer(ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'status', 'cost_per_delivery', 'cost_per_product', 'fixed_cost', 'created_at', 'updated_at']