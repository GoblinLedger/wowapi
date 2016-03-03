import requests
from wowapi import APIError

#: Table for converting currencies. Uses copper as the base unit.
CURRENCY_EXCHANGE = {
    'gold': 10000,
    'silver': 100,
    'copper': 1
}

FACTIONS = {
    '0': 'Alliance',
    '1': 'Horde'
}

GENDERS = {
    '0': 'Male',
    '1': 'Female'
}

def format_currency(copper, format='{gold}g {silver}s {copper}c'):
    """Takes a copper amount and formats it into a pretty string

    Given a integer copper amount, calculates the represented amount of gold,
    silver, and excess copper and returns a representational string based on a
    provided format. Defaults to {gold}g {silver}s {copper}c.
    """

    gold, silver, copper = convert_currency(copper)
    return format.format(gold=gold, silver=silver, copper=copper)

def convert_currency(copper):
    """Takes a copper ammout and converts it to a (gold,silver,copper) tuple"""

    gold = copper // CURRENCY_EXCHANGE['gold']
    copper = copper % CURRENCY_EXCHANGE['gold']
    silver = copper // CURRENCY_EXCHANGE['silver']
    copper = copper % CURRENCY_EXCHANGE['silver']
    return (gold, silver, copper)

def retrieve_auctions(auction_status, tries=2):
    """Given a auction status object, retreives all auctions in the snapshot"""

    # Copy the auction status object to only return a copy.
    data = dict(auction_status)

    for files in data['files']:
        # This often fails for unknown reasons. Trying again usually gets
        # it to work. Nasty hack, but not much choice.

        r = None
        while tries > 0:
            r = requests.get(files['url'])

            if r.status_code == 200:
                break
            tries = tries - 1

        if tries <= 0 and r.status_code != 200:
            raise APIError(r.status_code, r.text)

        files['data'] = r.json()

    return data

def format_character_race(api, charRace):
    """Returns a string identifying the character's race (i.e., Dwarf, Human, Undead)"""

    RACES = api.character_races()

    for race in RACES['races']:
        if race['id'] == charRace:
            return race['name']

    raise ValueError("{0} is not a valid race id.".format(charRace))

def format_character_class(api, charClass):
    """Returns a string identifying the character's class (i.e., Warlock, Paladin, Priest)"""

    CLASSES = api.character_classes()

    for wowClass in CLASSES['classes']:
        if wowClass['id'] == charClass:
            return wowClass['name']

    raise ValueError("{0} is not a valid class id.".format(charClass))

def format_character_faction(charFaction):
    """Returns a string identifying the character's faction (i.e., Horde/Alliance)"""

    if str(charFaction) not in FACTIONS:
        raise ValueError("{0} is not a valid faction for a character.  Value should be either 0 or 1.".format(charFaction))

    return FACTIONS[str(charFaction)]

def format_character_gender(charGender):
    """Returns a string identifying the character's gender (i.e, Male/Female)"""

    if str(charGender) not in GENDERS:
        raise ValueError("{0} is not a valid gender for a character.  Value should be either 0 or 1.".format(charGender))

    return GENDERS[str(charGender)]
