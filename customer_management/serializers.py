# """
# Serializers for the user profile app
#
# """
#
# from rest_framework.serializers import ModelSerializer
#
# from user_profile.models import User
#
#
# class UserProfileWriteSerializer(ModelSerializer):
#     """Write serializer for the user profile, used in create and update user profile"""
#
#     class Meta:
#         model = User
#         fields = "__all__"
