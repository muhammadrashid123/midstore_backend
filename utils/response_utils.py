"""
Utility functions for sending response
"""


import json

from django.http import HttpResponse
from lang.locale_utils import get_message


def create_message(data, status_code=None):
    """Create message utility for creating responses

    Args:
        data ([list]): [List of objects]
        status ([int], mandatory): [Internal system status code for the
                                    response defined in module locale]
                                    Defaults to None.

    Returns:
        [dict]: [Dict with status, message and data keys for client]
    """

    return {
        # internal system codes
        "status": status_code,
        # locale message in the system codes
        "message": get_message(status_code),
        "data": data,
    }


def create_response(
    response_body, http_status=None, header_dict={}, mime="application/json"
):
    """Create response utility for creating a generic response

    IMPORTANT : EXPECTS response_body param to be created and passed by
                create_message method.

    Args:
        response_body ([list]): [List of objects]
        http_status (int, optional): [The response HTTP Status code].
        header_dict (dict, optional): [Header data]. Defaults to {}.
        mime (str, optional): [Data type]. Defaults to 'application/json'.

    Returns:
        [HTTPResponse]: [The HTTP response]
    """

    if http_status is None:
        raise ValueError("No http status code provided")

    resp = HttpResponse(
        json.dumps(response_body), status=http_status, content_type=mime
    )

    for name, value in header_dict.items():
        resp[name] = value

    return resp
