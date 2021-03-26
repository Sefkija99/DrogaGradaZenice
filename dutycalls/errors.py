class DutyCallsClientError(Exception):
    """Base class for Client errors"""


class DutyCallsRequestError(DutyCallsClientError):
    """Error raised when there's a problem with the request that's being
    submitted."""


class DutyCallsAuthError(DutyCallsClientError):
    """Error raised when invalid credentials are used."""
