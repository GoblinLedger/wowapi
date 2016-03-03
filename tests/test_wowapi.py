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

def test_boss_list(api):
    ''' Retreive list of all bosses '''
    bosses = api.boss()

    assert 'bosses' in bosses

def test_boss_single(api):
    ''' Retreive a specific boss (Selin Fireheart) '''
    bossId = 24723
    bossName = 'Selin Fireheart'
    boss = api.boss(bossId)

    assert boss['id'] == bossId
    assert boss['name'] == bossName

def test_mount(api):
    ''' Get the list of mounts '''
    mounts = api.mount()
    assert 'mounts' in mounts

def test_zone_list(api):
    ''' Retreive full zone list '''
    zones = api.zone()
    assert 'zones' in zones

def test_zone_single(api):
    ''' Retreive a specfic zone (Magister's Terrace) '''
    zoneId = 4131
    zoneName = "Magister's Terrace"
    zone = api.zone(zoneId)
    assert zone['id'] == zoneId
    assert zone['name'] == zoneName
