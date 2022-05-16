"""
All views related to the user profile app

"""

from rest_framework.views import APIView
from user_profile.user_controller import UserProfileController


class UserProfileView(APIView):
    """CRUD View for the User model"""

    user_controller_obj = UserProfileController()

    def post(self, request):
        """Create new User"""

        return self.user_controller_obj.create_user(request)