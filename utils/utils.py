"""
Generic utility functions for the midstore

"""


import string, random


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """Generates random code of the specified length using given characters"""

    return "".join(random.choice(chars) for _ in range(size))


