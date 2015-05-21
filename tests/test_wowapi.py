import pytest
import os
from wowapi import APIError

@pytest.fixture
def api():
    import wowapi
    return wowapi.API(os.environ['WOWAPI_KEY'])


def test_invalid_key():
    ''' Test that wowapi throws a 403 error for invalid keys '''
    import wowapi
    api = wowapi.API("InvalidKeyForTesting")
    with pytest.raises(APIError) as excinfo:
        api.realm_status()
    assert excinfo.value.status_code == 403


def test_regions():
    ''' Get the realm status from each region to test region access'''
    import wowapi
    for region in wowapi.REGIONS:
        print(region)
        api = wowapi.API(os.environ['WOWAPI_KEY'], region=region)
        status = api.realm_status()
        assert 'realms' in status

def test_auction_data(api):
    ''' Retreive an auction status and a snapshot '''
    import wowapi.utility
    auction_status = api.auction_status('madoran')

    assert 'files' in auction_status

    snapshot = wowapi.utility.retrieve_auctions(auction_status)

    for snap in snapshot['files']:
        assert 'data' in snap
        assert 'auctions' in snap['data']

