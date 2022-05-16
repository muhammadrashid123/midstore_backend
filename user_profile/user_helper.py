"""
Helper class for the User Profile app

Helper logic facilitating UserProfileController is contained here

"""

from user_profile.models import User, UserType


class UserProfileHelper:
    """Helper class for the UserProfileController"""

    def validate_phone_number(self, phone_number):
        """Validates the phone number provided

        Args:
            phone_number ([str]): [The phone number the user entered]

        Returns:
            [Boolean, int]: [True in case phone number is valid, else system
                        error code]
        """

        # Length of phone number cannot be greater than 13
        if len(phone_number) > 13:
            return 106

        # Ascii value of all digits (0-9)
        digit_ascii = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

        # Check if characters are in the ascii range for digits
        for character in phone_number:
            if not ord(character) in digit_ascii:
                return 107

        return True

    def validate_update_user_payload(self, user, payload):
        """Validate the payload form data to check for correct values

        Args:
            payload ([dict]): [The payload recieved in form data]
            user ([dict]): [The user for which the payload is to be checked]


        Returns: System error code or True if data is valid
        """

        try:

            # Phone number provided should be unique
            if "contact_number" in payload and user.contact_number != payload["contact_number"]:

                # User is trying to set a phone number that is already
                # used by some other user
                if User.objects.filter(contact_number=payload["contact_number"]).first():
                    return 115

                # Validate length and characters of phone number
                status = self.validate_phone_number(
                    payload.get("contact_number")
                )
                if type(status).__name__ == "int":  # Return if error code
                    return status

            # Validate user type for supported types in UserType
            if "user_type" in payload and \
                    int(payload.get("user_type")) not in list(UserType.objects.all().values_list("id", flat=True)):
                return 101

            return True

        except Exception as ex:
            print(ex)
            return 1002
