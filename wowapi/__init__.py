import requests

REGIONS = {
    'US': 'https://us.api.battle.net/wow',
    'EU': 'https://eu.api.battle.net/wow',
    'KR': 'https://kr.api.battle.net/wow',
    'TW': 'https://tw.api.battle.net/wow'
}

CHARACTER_FIELDS = [
    "achievements",
    "appearance",
    "feed",
    "guild",
    "hunterPets",
    "items",
    "mounts",
    "pets",
    "petSlots",
    "progression",
    "pvp",
    "quests",
    "reputation",
    "stats",
    "talents",
    "titles",
    "audit"
]

GUILD_FIELDS = [
    "achievements",
    "members",
    "news",
    "challenge"
]

PVP_BRACKETS = [
    '2v2',
    '3v3',
    '5v5',
    'rbg'
]

class APIError(Exception):
    """Represents an Error accessing the community api for WoW"""

    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return "{0}: {1}".format(self.status_code, self.message)

class API:

    def __init__(self, apiKey, region='US', locale='en_US'):
        self.apiKey = apiKey
        self.locale = locale

        if region not in REGIONS:
            raise ValueError("Unknown region: {0}".format(region))

        self.region = region
        self.baseUrl = REGIONS[self.region]

    def get_resource(self, resourceURL, parameters=None):
        url = self.baseUrl + resourceURL
        payload = {'locale': self.locale, 'apikey': self.apiKey}

        if parameters is not None:
            # Merge parameters, overriding those that come from the call
            for key in parameters:
                payload[key] = parameters[key]

        r = requests.get(url, params=payload)
        return r.json()

    def achievement(self, id):
        resourceUrl = "/achievement/{0}".format(id)
        return self.get_resource(resourceUrl)

    def auction_status(self, realm):
        resourceUrl = "/auction/data/{0}".format(realm)
        return self.get_resource(resourceUrl)

    def battlepet_ability(self, abilityId):
        resourceUrl = "/battlePet/ability/{0}".format(abilityId)
        return self.get_resource(resourceUrl)

    def battlepet_species(self,speciesId):
        resourceUrl = "/battlePet/species/{0}".format(speciesId)
        return self.get_resource(resourceUrl)

    def battlepet_stats(self, speciesId, level=1, breedId=3, qualityId=1):
        if level > 25 or level < 1:
            raise ValueError("BattlePet levels must be in the range from 0 to 25")

        if qualityId > 6 or qualityId < 0:
            raise ValueError("BattlePet quality level must be in the range from 0 to 6")

        params = {
            "level": level,
            "breedId": breedId,
            "qualityId": qualityId
        }

        resourceUrl = "/battlePet/stats/{0}".format(speciesId)

        return self.get_resource(resourceUrl, parameters = params)

    def challenge_realm_leaderboard(self, realm):
        resourceUrl = "/challenge/{0}".format(realm)
        return self.get_resource(resourceUrl)

    def challenge_region_leaderboard(self):
        resourceUrl = "/challenge/region"
        return self.get_resource(resourceUrl)

    def character(self, realm, characterName, fields=None):
        params = {}
        if fields is not None:
            for field in fields:
                if field not in CHARACTER_FIELDS:
                    raise ValueError("{0} is not a valid field for a character.".format(field))
            params = {
                'fields': ','.join(fields)
            }

        resourceUrl = "/character/{0}/{1}".format(realm, characterName)
        return self.get_resource(resourceUrl, params)

    def guild(self, realm, guildName, fields=None):
        params = {}
        if fields is not None:
            for field in fields:
                if field not in GUILD_FIELDS:
                    raise ValueError("{0} is not a valid field for a guild.".format(field))
            params = {
                'fields': ','.join(fields)
            }

        resourceUrl = "/guild/{0}/{1}".format(realm, guildName)
        return self.get_resource(resourceUrl, params)

    def item(self, itemId):
        resourceUrl = "/item/{0}".format(itemId)
        return self.get_resource(resourceUrl)

    def item_set(self, setId):
        resourceUrl = "/item/set/{0}".format(setId)
        return self.get_resource(resourceUrl)

    def pvp_leaderboard(self, bracket):
        if bracket not in PVP_BRACKETS:
            raise ValueError("Unknown bracket type. Valid values are 2v2, 3v3, 5v5 and rbg.")

        resourceUrl = "/leaderboard/{0}".format(bracket)
        return self.get_resource(resourceUrl)

    def quest(self, questId):
        resourceUrl = "/quest/{0}".format(questId)
        return self.get_resource(resourceUrl)

    def realm_status(self):
        resourceUrl = "/realm/status"
        return self.get_resource(resourceUrl)

    def recipe(self, recipeId):
        resourceUrl = "/recipe/{0}".format(recipeId)
        return self.get_resource(resourceUrl)

    def spell(self, spellId):
        resourceUrl = "/spell/{0}".format(spellId)
        return self.get_resource(resourceUrl)

    def battlegroups(self):
        resourceUrl = "/data/battlegroups/"
        return self.get_resource(resourceUrl)

    def character_races(self):
        resourceUrl = "/data/character/races"
        return self.get_resource(resourceUrl)

    def character_classes(self):
        resourceUrl = "/data/character/classes"
        return self.get_resource(resourceUrl)

    def character_achievements(self):
        resourceUrl = "/data/character/achievements"
        return self.get_resource(resourceUrl)

    def guild_rewards(self):
        resourceUrl = "/data/guild/rewards"
        return self.get_resource(resourceUrl)

    def guild_perks(self):
        resourceUrl = "/data/guild/perks"
        return self.get_resource(resourceUrl)

    def guild_achievements(self):
        resourceUrl = "/data/guild/achievements"
        return self.get_resource(resourceUrl)

    def item_classes(self):
        resourceUrl = "/data/item/classes"
        return self.get_resource(resourceUrl)

    def talents(self):
        resourceUrl = "/data/talents"
        return self.get_resource(resourceUrl)

    def pet_types(self):
        resourceUrl = "/data/pet/types"
        return self.get_resource(resourceUrl)



