"""

All view related to the seller management

"""
from rest_framework.views import APIView

from seller_management.seller_management_controller import ShopController


class ShopView(APIView):

    shop_controller_obj = ShopController()

    def post(self, request):
        """ Create a Shop"""

        return self.shop_controller_obj.create_shop(request)

    def get(self, request):
        """Get a shop"""

        return self.shop_controller_obj.get_shop(request)

        """Get details of a User"""

        return self.shop_controller_obj.get_shop_details(request)