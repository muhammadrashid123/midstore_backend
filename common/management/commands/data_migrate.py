"""
Management command that migrates static data in database tables

"""

from django.core.management.base import BaseCommand
from user_profile.models import UserType, UserStatus


class Command(BaseCommand):
    help = "Data Migrations for midstore service"

    def handle(self, *args, **options):
        """Migration Data for UserStatus"""
        # active, inactive and deleted

        delete = UserStatus.objects.get_or_create(
            id=0,
            name="Delete",
            code="D"
        )

        active = UserStatus.objects.get_or_create(
            id=1,
            name="Active",
            code="A"
        )

        inactive = UserStatus.objects.get_or_create(
            id=2,
            name="Inactive",
            code="IA"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated: UserStatus"))

        """Migration Data for UserType"""
        # shop, seller and customer

        shop = UserType.objects.get_or_create(
            id=1,
            name="Shop",
            code="SH",
            description="This is the Shop user profile type"
        )

        seller = UserType.objects.get_or_create(
            id=2,
            name="Seller",
            code="SE",
            description="This is the Seller user profile type"
        )

        customer = UserType.objects.get_or_create(
            id=3,
            name="Customer",
            code="CUST",
            description="This is the Customer user profile type"
        )

        self.stdout.write(self.style.SUCCESS("Data migrated: UserType"))
