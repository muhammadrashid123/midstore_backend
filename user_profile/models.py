from django.db import models
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField
# Create your models here.


class UserStatus(models.Model):
    """Possible user statuses. i.e. Active, Inactive, Deleted etc."""

    name = models.CharField(max_length=30, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)


class UserType(models.Model):
    """Supported user types by the midstore backend. Data is inserted via
    data migration in the common app using `python manage.py data_migrate`
    management command"""

    name = models.CharField(max_length=30, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class User(AbstractUser):
    """User model extending Django's default user model.
    Main User model for the midstore backend. User types e.g. Seller, Customer etc
    are maintained using a UserType model through a foreign key relation
    """

    # User identifier
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    address = models.TextField()
    address_2 = models.TextField(null=True, blank=True)
    contact_number = models.CharField(unique=True, max_length=200, null=False, blank=False)  # required
    gender = models.CharField(max_length=50, null=True, blank=True)

    image = models.ImageField(upload_to="user_profile_images", null=True)

    cnic = models.CharField(max_length=30, null=True, blank=True)

    user_type = models.ForeignKey(
        UserType, null=True, blank=True, on_delete=models.PROTECT
    )

    status = models.ForeignKey(
        UserStatus, null=True, blank=True, on_delete=models.PROTECT
    )

    # shop = models.ForeignKey(Shop, null=True, blank=True, on_delete=models.CASCADE)  # Shop foreign key
    # Forgot password verification code
    forgot_pwd_email_code = models.CharField(max_length=20, null=True, blank=True)

    # Is forgot pwd code verified
    is_forgot_pwd_code_verified = models.BooleanField(default=False)

    # Is user email verified
    is_email_verified = models.BooleanField(default=False)

    # Use EMAIL insted of USERNAME
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']