"""
Models related to the authentication app

"""

from django.db import models
from user_profile.models import User


class Token(models.Model):
    """Token model for the authentication system"""

    token = models.CharField(max_length=100,
                             default="",
                             null=False,
                             blank=False
                             )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    is_valid = models.BooleanField(default=True)
