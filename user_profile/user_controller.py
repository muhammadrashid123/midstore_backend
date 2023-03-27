"""
Controller class for the User Profile app

All business logic related to user management is contained here

"""
import uuid

from django.db.models import Q

from user_profile.models import User, UserType
from user_profile.serializers import (UserProfileReadSerializer,
                                      UserProfileWriteSerializer)
from user_profile.user_helper import UserProfileHelper
from utils.request_utils import get_query_param_or_default
from utils.response_utils import create_message, create_response
from django.contrib.auth.hashers import make_password
from django.db import transaction

import logging
import traceback

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
            logging.exception(str(ex))
            # traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)

    def update_user_profile(self, request):
        """ Updating User """
        try:
            # contact_number is mandatory in query params
            if not get_query_param_or_default(request, "contact_number", None):
                return create_response(create_message([], 105), 400)

            # Get mutable copy of request payload
            payload = request.data.copy()

            user = User.objects.filter(
                contact_number=get_query_param_or_default(request, "contact_number", None)).first()

            # If user does not exist
            # if not user and user.status == 0:
            if not user:
                return create_response(create_message([], 104), 404)


            # contact number cannot be updated
            payload.pop("contact_number", None)

            # Email cannot be updated
            payload.pop("email", None)
            # Password cannot be updated
            payload.pop("password", None)

            # pop status if status 0 is passed
            payload.pop("status") if payload.get("status", None) and int(payload.get("status")) == 0 else ""

            # Validate payload keys
            status = self.user_helper.validate_update_user_payload(user, payload)
            if type(status).__name__ == "int":
                return create_response(create_message([], status), 400)

            serialized = UserProfileWriteSerializer(data=payload, partial=True)

            if serialized.is_valid():
                with transaction.atomic():
                    serialized.update(user, serialized.validated_data)
            read_serialized = UserProfileReadSerializer(user)

            return create_response(create_message(read_serialized.data, 109), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)

    def get_user_details(self, request):
        """ Getting details of user """
        try:
            # contact_number is mandatory in query params
            if not get_query_param_or_default(request, "contact_number", None):
                return create_response(create_message([], 105), 400)

            user_obj = User.objects.filter(contact_number=get_query_param_or_default(request, "contact_number", None)).first()

            # If user does not exist
            if not user_obj:
                return create_response(create_message([], 104), 404)

            serialized = UserProfileReadSerializer(user_obj)

            return create_response(create_message([serialized.data], 1000), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)

    def delete_user(self, request):
        """" Deleting the User """
        try:

            if not get_query_param_or_default(request, "contact_number", None):
                return create_response(create_message([], 105), 400)

            user_obj = User.objects.filter(
                contact_number=get_query_param_or_default(request, "contact_number", None)).first()

            # If user does not exist
            if not user_obj:
                return create_response(create_message([], 104), 404)

            # Set user status to deleted
            user_obj.status_id = 0

            # append deleted and uuid at the end of email, contact number and username so the email ,contact number and
            # username can be used again for user creation
            user_obj.email = str(user_obj.email) + "deleted" + str(uuid.uuid4())
            user_obj.contact_number = str(user_obj.contact_number) + "deleted" + str(uuid.uuid4())
            user_obj.username = str(user_obj.username) + "deleted" + str(uuid.uuid4())

            user_obj.save()

            return create_response(create_message([], 309), 200)

        except Exception as ex:
            logging.exception(str(ex))
            traceback.print_ex()
            return create_response(create_message([str(ex)], 1002), 500)
