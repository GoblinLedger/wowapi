def format_currency(copper, format='{gold}g {silver}s {copper}c'):
    """Takes a copper amount and formats it into a pretty string

    Given a integer copper amount, calculates the represented amount of gold,
    silver, and excess copper and returns a representational string based on a
    provided format. Defaults to {gold}g {silver}s {copper}c.
    """

    gold = copper // 10000
    copper = copper % 10000
    silver = copper // 100
    copper = copper % 100
    return format.format(gold=gold, silver=silver, copper=copper)
