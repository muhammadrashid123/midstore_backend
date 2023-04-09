"""
Generic utility functions for the midstore

"""

import string, random
from datetime import timedelta
from django.utils import timezone
from midstore_backend.settings import get_secret


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """Generates random code of the specified length using given characters"""

    return "".join(random.choice(chars) for _ in range(size))

def is_token_expired(token):
    expiry = get_secret("AUTH_TOKEN_EXPIRY_IN_SECONDS")
    min_age = timezone.now() - timedelta(seconds=expiry)
    expired = token.created < min_age
    return expired



