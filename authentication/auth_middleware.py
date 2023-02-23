"""
Custom middleware for validating token received in the request header.
After validating the token against User, the user object is added
to request.user

"""
import logging
import traceback

from django.core.wsgi import get_wsgi_application
from django.utils.deprecation import MiddlewareMixin

from authentication.models import Token
from user_profile.serializers import UserProfileReadSerializer
from utils.response_utils import create_response, create_message


class TokenValidationMiddleware(MiddlewareMixin):
    """Custom middleware hook in the django middlewares for token validation"""

    def __init__(self, get_response):
        """Initialization method for the object. Initialized with the next
        middleware/view to be executed.

        Args:
            get_response ([middleware/view]): [The middleware that is next
            in line to be executed in the settings and the api view in case
            this is the last middleware.

                THIS ARGUMENT IS PASSED BY DJANGO AUTOMATICALLY
            ]
        """

        # One-time configuration and initialization.
        self.get_response = get_response

        # URLs allowed without token in request header
        # Format is tuple
        # (URL, METHOD)

        self.BYPASS_TOKEN_CHECK_URLS = [

            # User Profile
            ("/midstore/user-profile/user", "POST"),

            # Authentication
            ("/midstore/authentication/user/login", "POST"),

        ]

    def process_request(self, request):
        """Process request hook called after initializing
        middleware and before process view method is called.

        Process request method verifies the token and
        adds the user to the session if token is valid.
        """

        try:

            # If request path in bypass urls list
            if (request.path, request.method) in self.BYPASS_TOKEN_CHECK_URLS:
                return

            # Populate app registry so we can access our models
            application = get_wsgi_application()

            # Check if the token is provided in the header
            auth_header = request.META.get("HTTP_AUTHORIZATION", None)
            if not auth_header:
                return create_response(create_message([], 113), 400)

            header_token = str(auth_header).split(" ")[-1]

            user_token_obj = Token.objects.filter(
                token=header_token,
                is_valid=True
            ).first()

            # Token not found, it means that the token is invalid
            if not user_token_obj:
                return create_response(create_message([], 113), 400)

            # Add the login user object to the request.user variable
            # So we can access the logged in user object conveniently
            request.session["user"] = UserProfileReadSerializer(user_token_obj.user).data

            return

        except Exception as ex:
            print(ex)
            logging.exception(str(ex))
            traceback.print_exc()
            return create_response(create_message([str(ex)], 1002), 500)

