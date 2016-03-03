import pytest
import wowapi.utility

def test_currency_conversion():
    gold,silver,copper = wowapi.utility.convert_currency(7540984)
    assert gold == 754
    assert silver == 9
    assert copper == 84

def test_format_character_faction():
    for faction in wowapi.utility.FACTIONS:
        assert wowapi.utility.format_character_faction(faction) == wowapi.utility.FACTIONS[faction]

    with pytest.raises(ValueError):
        wowapi.utility.format_character_faction("unknownFaction")


def test_format_character_gender():
    for gender in wowapi.utility.GENDERS:
        assert wowapi.utility.format_character_gender(gender) == wowapi.utility.GENDERS[gender]

    with pytest.raises(ValueError):
        wowapi.utility.format_character_gender("unknownGender")
