"""
Controller class for the authentication app

All business logic related to authentication is contained here

"""
import logging
import traceback
import uuid

from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from user_profile.models import User
from utils.response_utils import create_response, create_message
from utils.utils import is_token_expired
from midstore_backend.settings import get_secret
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
            ).first()

            if not user_token_obj:  # Create new token object in case of first user login
                user_token_obj = Token.objects.create(
                    key=(str(uuid.uuid4())).replace("-", ""),
                    user=user
                )
                
            expired  = is_token_expired(user_token_obj)
            if expired:
                user_token_obj.delete()
                user_token_obj = Token.objects.create(user=user)
                
            delta = user_token_obj.created + timedelta(seconds=get_secret("AUTH_TOKEN_EXPIRY_IN_SECONDS"))

            response_data = {
                "Token": user_token_obj.key,
                "expired_in_seconds":(delta - timezone.now()).total_seconds()
            }

            return create_response(create_message([response_data], 112), 200)

        except Exception as exc:
            logging.exception(str(exc))
            traceback.print_exc()
            return create_response(create_message([str(exc)], 1002), 500)

    def refresh_token(self, key):
        # Mandatory keys in the request payload
        mandatory_keys = [
            "key"
        ]
        response_data = {
            "Refresh Token":"",
            "expired_in_seconds":""
        }
        try:
            if not key:
                return create_response(create_message(mandatory_keys, 100), 400)
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            return create_response(create_message([], 318), 200)

        if not token.user.is_active:
           return create_response(create_message([], 319), 200)

        expired = is_token_expired(token)
        if expired:
            token.delete()
            token = Token.objects.create(user=token.user)
            
        delta = token.created + timedelta(seconds=get_secret("AUTH_TOKEN_EXPIRY_IN_SECONDS"))
        response_data['Refresh Token'] = token.__dict__['key']
        response_data['expired_in_seconds'] = (delta - timezone.now()).total_seconds()
        return create_response(create_message([response_data], 1000), 200)