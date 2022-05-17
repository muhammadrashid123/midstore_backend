"""
Serializers for seller management

"""

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from seller_management.models import Shop


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
