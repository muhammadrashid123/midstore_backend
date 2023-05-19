from cart_management.models import Cart, Checkout
from rest_framework import serializers
from uuid import UUID




class CartSerializer(serializers.ModelSerializer):
    """ Serialized cart data """
    product_name = serializers.SerializerMethodField()
    
    def get_product_name(self, obj):
        return obj.product.title
    
    class Meta:
        model = Cart
        fields = '__all__'

        
    def create(self, validated_data):
        cart_obj = Cart.objects.create(**validated_data)
        return cart_obj
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {'uuid':representation['uuid'],'product_name': representation['product_name'], 'quantity': representation['quantity']}
    
class CheckoutSerializer(serializers.ModelSerializer):
    """ Serialized checkout data """
    
    class Meta:
        model = Checkout
        fields = "__all__"