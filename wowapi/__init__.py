import requests

"""The available regions"""
REGIONS = {
    'US': 'https://us.api.battle.net/wow',
    'EU': 'https://eu.api.battle.net/wow',
    'KR': 'https://kr.api.battle.net/wow',
    'TW': 'https://tw.api.battle.net/wow'
}

"""The available fields for use to get more detailed information for a specific character"""
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
    "statistics",
    "stats",
    "talents",
    "titles",
    "audit"
]

"""The available fields for use to get more detailed information for a specific guild"""
GUILD_FIELDS = [
    "achievements",
    "members",
    "news",
    "challenge"
]

"""The available PvP brackets"""
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

        # Raise an api error for all non-200 status codes
        if r.status_code != 200:
            raise APIError(r.status_code, r.text)

        return r.json()

    def achievement(self, id):
        """Returns a specific achievement for the given id"""
        resourceUrl = "/achievement/{0}".format(id)
        return self.get_resource(resourceUrl)

    def auction_status(self, realm):
        """Returns a link to the latest auction house data dump for the given realm"""
        resourceUrl = "/auction/data/{0}".format(realm)
        return self.get_resource(resourceUrl)

    def battlepet_ability(self, abilityId):
        """Returns data about a specific battle pet ability for the given id"""
        resourceUrl = "/battlePet/ability/{0}".format(abilityId)
        return self.get_resource(resourceUrl)

    def battlepet_species(self,speciesId):
        """Returns data about an indiviual pet specied for the given specied id"""
        resourceUrl = "/battlePet/species/{0}".format(speciesId)
        return self.get_resource(resourceUrl)

    def battlepet_stats(self, speciesId, level=1, breedId=3, qualityId=1):
        """Returns detailed information about a given species of pet"""
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
        """Returns data about the challenge realm leaderboard for a given realm"""
        resourceUrl = "/challenge/{0}".format(realm)
        return self.get_resource(resourceUrl)

    def challenge_region_leaderboard(self):
        """Returns data about the challenge realm leaderboard for the region you choose to use"""
        resourceUrl = "/challenge/region"
        return self.get_resource(resourceUrl)

    def character(self, realm, characterName, fields=None):
        """Returns character information based on the given realm/characterName """
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
        """Returns guild information based on the given realm/guildName"""
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
        """Returns detailed item information for the given itemId"""
        resourceUrl = "/item/{0}".format(itemId)
        return self.get_resource(resourceUrl)

    def item_set(self, setId):
        """Returns detailed item information for the given item setId"""
        resourceUrl = "/item/set/{0}".format(setId)
        return self.get_resource(resourceUrl)

    def pvp_leaderboard(self, bracket):
        """Returns PvP leaderboard information for the given bracket"""
        if bracket not in PVP_BRACKETS:
            raise ValueError("Unknown bracket type. Valid values are 2v2, 3v3, 5v5 and rbg.")

        resourceUrl = "/leaderboard/{0}".format(bracket)
        return self.get_resource(resourceUrl)

    def quest(self, questId):
        """Returns metadata for the given questId"""
        resourceUrl = "/quest/{0}".format(questId)
        return self.get_resource(resourceUrl)

    def realm_status(self):
        """Returns realm status information for all realms"""
        resourceUrl = "/realm/status"
        return self.get_resource(resourceUrl)

    def recipe(self, recipeId):
        """Returns basic recipe information for the given recipeId"""
        resourceUrl = "/recipe/{0}".format(recipeId)
        return self.get_resource(resourceUrl)

    def spell(self, spellId):
        """Returns some information for the given spellId"""
        resourceUrl = "/spell/{0}".format(spellId)
        return self.get_resource(resourceUrl)

    def battlegroups(self):
        """Returns a list of battlegroups for the region"""
        resourceUrl = "/data/battlegroups/"
        return self.get_resource(resourceUrl)

    def character_races(self):
        """Returns a list of each race and their associated faction, name, uniqueId, and skin"""
        resourceUrl = "/data/character/races"
        return self.get_resource(resourceUrl)

    def character_classes(self):
        """Returns a list of character classes"""
        resourceUrl = "/data/character/classes"
        return self.get_resource(resourceUrl)

    def character_achievements(self):
        """Returns a list of all achievements that characters can earn"""
        resourceUrl = "/data/character/achievements"
        return self.get_resource(resourceUrl)

    def guild_rewards(self):
        """Returns a list of all guild rewards"""
        resourceUrl = "/data/guild/rewards"
        return self.get_resource(resourceUrl)

    def guild_perks(self):
        """Returns a list of all guild perks"""
        resourceUrl = "/data/guild/perks"
        return self.get_resource(resourceUrl)

    def guild_achievements(self):
        """Returns a list of all achievements that a guild can earn"""
        resourceUrl = "/data/guild/achievements"
        return self.get_resource(resourceUrl)

    def item_classes(self):
        """Returns a list of item classes"""
        resourceUrl = "/data/item/classes"
        return self.get_resource(resourceUrl)

    def talents(self):
        """Returns a list of talents, specs, and glyphs for each class"""
        resourceUrl = "/data/talents"
        return self.get_resource(resourceUrl)

    def pet_types(self):
        """Returns different battle pet types, including what they are strong and weak against"""
        resourceUrl = "/data/pet/types"
        return self.get_resource(resourceUrl)

    def mount(self):
        """Returns a list of all supported mounts"""
        resourceUrl = "/mount/"
        return self.get_resource(resourceUrl)

    def zone(self, id=None):
        """Returns a specific zone (zone being a dungeon or raid in this context) or a list of all supported zones"""
        if id is not None:
            resourceUrl = "/zone/{0}".format(id)
            return self.get_resource(resourceUrl)

        resourceUrl = "/zone/"
        return self.get_resource(resourceUrl)

    def boss(self, id=None):
        """Returns a specific boss (boss being a boss encounter, which may include more than one NPC) or a list of all supported bosses"""
        if id is not None:
            resourceUrl = "/boss/{0}".format(id)
            return self.get_resource(resourceUrl)

        resourceUrl = "/boss/"
        return self.get_resource(resourceUrl)
