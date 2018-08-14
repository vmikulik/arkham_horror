# terminal interface for drawing chaos tokens.

import argparse
from os import system
import chaos

parser = argparse.ArgumentParser(description="Digital chaos tokens for Arkham Horror LCG.")

parser.add_argument('campaign', metavar='CAMPAIGN', 
                    choices=chaos.campaign_settings.keys(),
                    help='The name of the campaign being played')
parser.add_argument('difficulty', metavar='DIFFICULTY', 
                    choices=["easy", "standard", "hard", "expert"],
                    help='The difficulty level')
parser.add_argument('-a', '--add', action='append', dest='add',
                    help='Add this token to the specified pool')
parser.add_argument('-r', '--rm', action='append', dest='rm',
                    help='Remove this token from the specified pool')

if __name__ == '__main__':
    # parse args and prepare bag
    args = parser.parse_args()
    bag = chaos.Bag(args.campaign, args.difficulty)
    if args.add is not None:
        for value in args.add:
            bag.add(value)
    if args.rm is not None:
        for value in args.rm:
            bag.remove(value)
    
    # start game
    running = True
    while running:
        cmd = input("").lower()
        system('clear')
        if cmd == 'q' or cmd == 'quit':
            running = False
            break
        else:
            print()
            print("🎲:  "+ bag.draw())
            print()

    