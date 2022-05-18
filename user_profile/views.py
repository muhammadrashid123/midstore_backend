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

    def patch(self, request):
        """Update a User"""

        return self.user_controller_obj.update_user_profile(request)

    def get(self, request):
        """Get details of a User"""

        return self.user_controller_obj.get_user_details(request)

    def delete(self,request):
        """Delete existing User"""

        return self.user_controller_obj.delete_user(request)