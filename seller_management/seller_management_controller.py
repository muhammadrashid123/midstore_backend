"""
Controller class for the Seller Management app

All business logic related to seller management is contained here

"""
from seller_management.serializers import ShopWriteSerializer, ShopProfileReadSerializer
from utils.response_utils import create_response, create_message


class ShopController:
    """
    Controller class for the shop
    """

    def create_shop(self, request):
        """
        Create a shop

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]

        """
        try:
            # Get a mutable copy of request payload
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "name",
                "shop_type",
                "address"
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            serialized = ShopWriteSerializer(data=payload)

            if serialized.is_valid():

                shop_obj = serialized.save()

            else:  # There were errors while serializing the payload
                return create_response(create_message([serialized.errors], 102), 400)

            serialized = ShopProfileReadSerializer(shop_obj)

            return create_response(create_message([serialized.data], 103), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)


