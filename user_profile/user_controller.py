"""
Controller class for the User Profile app

All business logic related to user management is contained here

"""

from user_profile.models import UserType
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)
from user_profile.user_helper import UserProfileHelper
from utils.response_utils import create_message, create_response
from django.contrib.auth.hashers import make_password


class UserProfileController:
    """Controller for the business logic of user profile app"""

    user_helper = UserProfileHelper()

    def create_user(self, request):
        """Create user with the given request payload

        Args:
            request ([WSGIRequest]): [The request made by the client]

        Returns:
            [Obj]: [Response Object with keys: status, message and data]
        """

        try:

            # Get mutable copy of request.data
            payload = request.data.copy()

            # Mandatory keys in the request payload
            mandatory_keys = [
                "user_type",  # The type of user to be created
                "password",
                "contact_number"
            ]

            # Check if all mandatory keys exist in the request payload
            if not all(key in list(payload.keys()) for key in mandatory_keys):
                return create_response(create_message(mandatory_keys, 100), 400)

            # Check if user type id is in the supported user types model
            if not int(payload.get("user_type")) in list(UserType.objects.all().values_list("id", flat=True)):
                return create_response(create_message([], 101), 400)

            # by default user status will be Active i.e. 1
            payload["status"] = 1

            # Hash plain text password
            payload["password"] = make_password(payload.get("password"))

            serialized = UserProfileWriteSerializer(data=payload)

            if serialized.is_valid():  # check if payload data is correct
                user = serialized.save()
            else:  # There were errors while serializing the payload
                return create_response(create_message([serialized.errors], 102), 400)

            serialized = UserProfileReadSerializer(user)

            return create_response(create_message([serialized.data], 108), 201)

        except Exception as ex:
            print(ex)
            return create_response(create_message([str(ex)], 1002), 500)
