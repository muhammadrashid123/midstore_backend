"""
All views related to the user profile app

"""


from rest_framework.views import APIView
from authentication.auth_controller import AuthController
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from utils.utils import is_token_expired
from utils.response_utils import create_message

class UserAuthView(APIView):
    """Auth view for User authentication"""

    authentication_controller = AuthController()

    def post(self, request):
        """Login a User and provide client with a token,
        which they have to send in all the requests to prove
        that they are authenticated users"""

        return self.authentication_controller.user_login(request)
class AuthRefreshToken(APIView):
    """Auth view to generate refresh auth token."""
    authentication_controller = AuthController()
    
    def post(self, request):
        """ Get refresh token for user."""
        
        return self.authentication_controller.refresh_token(request.data.get('key',None))
    
class ExpiringTokenAuthentication(TokenAuthentication):
    """Same as in DRF, but also handle Token expiration.
    
    Raise AuthenticationFailed as needed, which translates 
    to a 401 status code automatically.
    """
    authentication_controller = AuthController()
    
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(create_message([],113))

        if not token.user.is_active:
            message = "User inactive or deleted"
            raise AuthenticationFailed(create_message([],113,message))

        expired = is_token_expired(token)
        if expired:
            message="Token has been expired"
            raise AuthenticationFailed(create_message([],113,message))

        return (token.user, token)