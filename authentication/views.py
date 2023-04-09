"""
All views related to the user profile app

"""


from rest_framework.views import APIView
from authentication.auth_controller import AuthController


class UserAuthView(APIView):
    """Auth view for User authentication"""

    authentication_controller = AuthController()

    def post(self, request):
        """Login a User and provide client with a token,
        which they have to send in all the requests to prove
        that they are authenticated users"""

        return self.authentication_controller.user_login(request)
class AuthToken(APIView):
    """Auth view to generate refresh auth token."""
    authentication_controller = AuthController()
    
    def post(self, request):
        """ Get refresh token for user."""
        
        return self.authentication_controller.refresh_token(request.data.get('key',None))