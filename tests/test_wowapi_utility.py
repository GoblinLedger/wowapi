import pytest
import wowapi.utility

def test_currency_conversion():
    gold,silver,copper = wowapi.utility.convert_currency(7540984)
    assert gold == 754
    assert silver == 9
    assert copper == 84
