"""
Controller class for the Seller Management app

All business logic related to seller management is contained here

"""
import logging
import traceback

from seller_management.models import Seller_Shop
from seller_management.serializers import ShopWriteSerializer, ShopReadSerializer
from user_profile.models import User
from utils.request_utils import get_query_param_or_default
from utils.response_utils import create_response, create_message


class ShopController:
    """
    Controller class for the shop
    """


    def create_user(self, request):
        """Create user with the given request payload

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

            serialized = ShopReadSerializer(shop_obj)

            return create_response(create_message([serialized.data], 103), 201)

        except Exception as exc:
            logging.exception(str(exc))
            traceback.print_exc()
            return create_response(create_message([str(exc)], 1002), 500)

    def get_shop(self, request):
        """Get details of a shop"""
        try:

            # uuid is mandatory in query params
            if not get_query_param_or_default(request, "uuid", None):
                return create_response(create_message([], 110), 400)
            shop_obj = Seller_Shop.objects.filter(uuid=get_query_param_or_default(request, 'uuid', None)).first()
            if not shop_obj:
                return create_response(create_message([], 302), 404)
            serialized = ShopReadSerializer(shop_obj)

            return create_response(create_message(serialized.data, 1000), 200)

        except Exception as exc:
            logging.exception(str(exc))
            traceback.print_exc()
            return create_response(create_message([str(exc)], 1002), 500)