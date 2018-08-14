# this file provides functions for drawing chaos tokens.
# coding=utf-8

from json import load
from random import choice
campaign_settings = load(open('campaignsettings.json'))

class Token():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "Token({})".format(self.value)
    
    def __str__(self):
        if type(self.value) is int:
            return str(self.value)
        else:
            return Token.to_symbol(self.value)

    def __eq__(self, other):
        return self.value == other.value if isinstance(other, Token) else False
    
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

class Bag():
    def __init__(self, campaign=None, difficulty=None, tokens=None):
        if difficulty == None or campaign == None:
            if tokens == None:
                tokens = []
            self.tokens = tokens
        else:
            campaign, difficulty = campaign.lower(), difficulty.lower()
            if campaign not in campaign_settings: 
                raise Error("invalid campaign")
            elif difficulty not in ["easy", "standard", "hard", "expert"]:
                raise Error("invalid difficulty")
            else:
                self.tokens = [Token(value) for value in campaign_settings[campaign][difficulty]]
    
    def __repr__(self):
        return "Bag({})".format(repr(self.tokens))

    def __str__(self):
        return "Bag({})".format(",".join([str(token) for token in self.tokens]))

    def draw(self):
        print(str(choice(self.tokens)))

    def add(self, value):
        self.tokens.append(Token(value))

    def remove(self, value):
        self.tokens.remove(Token(value))

if __name__ == '__main__':
    bag = Bag()
    print("Empty bag: " + str(bag))
    bag = Bag([])
    print("Empty bag: " + str(bag))
    bag = Bag("night of the zealot", "easy")
    print("Night of the Zealot easy bag: " + str(bag))
    bag = Bag("the dunwich legacy", "standard")
    print("The Dunwich Legacy standard bag: " + str(bag))
    bag.add('old one')
    bag.remove('tentacles')
    print("with old one but not tentacles: " + str(bag))


    