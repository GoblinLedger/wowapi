
#: Table for converting currencies. Uses copper as the base unit.
CURRENCY_EXCHANGE = {
    'gold': 10000,
    'silver': 100,
    'copper': 1
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