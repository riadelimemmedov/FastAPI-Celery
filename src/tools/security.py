# Third party modules
from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security, status

# local modules
from src import config

# Constants
API_KEY_HEADER = APIKeyHeader(name="X-API-Key")
""" Using API key authentication. """


# !---------------------------------------------------------
#
def validate_authentication(api_key: str = Security(API_KEY_HEADER)):
    """Validate API key authentication.

    :param api_key: Authentication credentials.
    :raise HTTPException(401): When incorrect API key is supplied.
    """

    if api_key != config.service_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
            headers={"WWW-Authenticate": "X-API-Key"},
        )
