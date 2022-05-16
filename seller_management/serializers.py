"""
Serializers for sellers

"""

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from customer_management.models import User
from seller_management.models import Shop


class SellerProfileWriteSerializer(ModelSerializer):
    """Write serializer for the seller profile, used in create and update seller profile"""

    class Meta:
        model = User
        fields = "__all__"


class SellerProfileReadSerializer(ModelSerializer):
    """Read serializer for the seller profile, used where seller profile needs to be serialized"""

    uuid = SerializerMethodField()


    def get_uuid(self, obj):
        if obj.uuid:
            return str(obj.uuid)

    class Meta:
        model = User
        fields = "__all__"



class ShopWriteSerializer(ModelSerializer):
    """Write serializer for the seller profile, used in create and update seller profile"""

    class Meta:
        model = Shop
        fields = "__all__"


class ShopProfileReadSerializer(ModelSerializer):
    """Read serializer for the seller profile, used where seller profile needs to be serialized"""

    uuid = SerializerMethodField()

    user = SerializerMethodField()

    def get_uuid(self, obj):
        if obj.uuid:
            return str(obj.uuid)

    def get_user(self, obj): # foreign key user
        if obj.user:
            return str(obj.user.uuid)

    class Meta:
        model = User
        fields = "__all__"

