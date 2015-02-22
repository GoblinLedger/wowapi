import pytest
import os
from wowapi import APIError

@pytest.fixture
def api():
    import wowapi
    return wowapi.API(os.environ['WOWAPI_KEY'])


def test_realm_status(api):
    status = api.realm_status()
    assert 'realms' in status
