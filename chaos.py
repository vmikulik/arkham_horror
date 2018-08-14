# this file provides functions for drawing chaos tokens.

from campaignsettings import campaign_defaults, difficulty_levels

class Token():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Token({})".format(value)
    
    def __str__(self):
        if type(value) is int:
            return str(value)
        if type(value) is str:
            return T.to_symbol(value)
    
    @staticmethod
    def to_symbol(string):
        dictionary = {
            'skull':'💀',
            'cult':'🧛‍',
            'tentacles':'🦑',
            'stone':'🍞',
            'old one':'🐲',
            'elder sign':'🌟'
        }
        string = string.lower()
        if string in dictionary:
            return dictionary[string]
        else:
            return string

class ChaosBag():
    def __init__(self, campaign=None, difficulty=None):
        campaign, difficulty = campaign.lower(), difficulty.lower()
        if difficulty == None or campaign == None:
            self.tokens = []
        elif campaign not in campaign_defaults or difficulty not in difficulty_levels:
                raise Error("bad input")
        else:
            self.tokens = [Token(value) for value in ChaosBag.campaign_defaults[campaign][difficulty]]


    