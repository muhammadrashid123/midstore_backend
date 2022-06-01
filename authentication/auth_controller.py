"""
Controller class for the authentication app

All business logic related to authentication is contained here

"""
import logging
import traceback
import uuid

from django.contrib.auth.hashers import check_password

from authentication.models import Token
from user_profile.models import User
from utils.response_utils import create_response, create_message


class AuthController:
    """Controller for authentication related logic"""

    def user_login(self, request):
        """Validate credentials and generate a login token"""

        try:
            payload = request.data.copy()

            email = payload.get("email")

            if not email:
                # Mandatory keys in the request payload
                mandatory_keys = [
                    "contact_number",
                    "password"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(contact_number=payload.get("contact_number")).first()

                if not user:  # Invalid contact_number
                    return create_response(create_message([], 111), 401)

            else:
                # Mandatory keys in the request payload
                mandatory_keys = [
                    "email",
                    "password"
                ]

                # Check if all mandatory keys exist in the request payload
                if not all(key in list(payload.keys()) for key in mandatory_keys):
                    return create_response(create_message(mandatory_keys, 100), 400)

                user = User.objects.filter(email=payload.get("email")).first()

                if not user:  # Invalid email
                    return create_response(create_message([], 111), 401)

            # Check user password
            if not check_password(payload.get("password"), user.password):
                return create_response(create_message([], 111), 401)

            # Search for existing token
            user_token_obj = Token.objects.filter(
                user=user,
                is_valid=True
            ).first()

            if not user_token_obj:  # Create new token object in case of first user login
                user_token_obj = Token.objects.create(
                    token=(str(uuid.uuid4()) + str(uuid.uuid4())).replace("-", ""),
                    user=user
                )
            else:
                # Create new token for user
                user_token_obj.token = (str(uuid.uuid4()) + str(uuid.uuid4())).replace("-", "")
                user_token_obj.is_valid = True
                user_token_obj.save()

            response_data = {
                "Token": user_token_obj.token
            }

            return create_response(create_message([response_data], 112), 200)

        except Exception as exc:
            logging.exception(str(exc))
            traceback.print_exc()
            return create_response(create_message([str(exc)], 1002), 500)
