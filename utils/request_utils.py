"""
Utility functions related to client requests

"""

from user_profile.models import User


def get_query_param_or_default(request, key, default):
    """

    @param request: request object
    @type request: request
    @param key: key to get data from
    @type key: str
    @param default: default variable to return if key is empty or doesn't exist
    @type default: str/None
    @return: key
    @rtype: str/None
    """
    if key in request.query_params:
        key = request.query_params.get(key)
        if key:
            return key
    return default


def get_user_from_session(request):
    """Extracts the User object from the current session"""

    return User.objects.get(email=request.session["user"]["email"])


def get_user_from_session_contact_number(request):
    """Extracts the User object from the current session"""

    return User.objects.get(contact_number=request.session["user"]["contact_number"])
