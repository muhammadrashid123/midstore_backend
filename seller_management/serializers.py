"""
Serializers for seller management

"""

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from seller_management.models import Shop
from user_profile.models import User


class ShopWriteSerializer(ModelSerializer):
    """Write serializer for the shop, used in create and update shop profile"""

    class Meta:
        model = Shop
        fields = "__all__"


class ShopReadSerializer(ModelSerializer):
    """Read serializer for the shop, used where shop needs to be serialized"""

    uuid = SerializerMethodField()

    def get_uuid(self, obj):
        if obj.uuid:
            return str(obj.uuid)

    class Meta:
        model = Shop
        fields = "__all__"


class ShopUserProfileReadSerializer(ModelSerializer):
    """Read serializer for the shop user profile, used where user profile needs to be serialized"""
    # uuid = SerializerMethodField()
    #
    # shop = SerializerMethodField()
    #
    # def get_uuid(self, obj):
    #     if obj.uuid:
    #         return str(obj.uuid)
    #
    # def get_shop(self, obj):
    #     shop_detail = {}
    #     if obj.shop:
    #         shop_detail['uuid'] = obj.shop.uuid
    #         shop_detail['name'] = obj.shop.name
    #         shop_detail['logo'] = obj.shop.logo
    #         shop_detail['shop_type'] = obj.shop.shop_type
    #         shop_detail['address'] = obj.shop.address
    #         shop_detail['description'] = obj.shop.description
    #         return str(shop_detail)

    class Meta:
        model = User
        exclude = ('shop', )
        # fields = "__all__"
