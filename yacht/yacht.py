"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):

    print(dice)
    print(category)
    points = 0

    if category == 12:
        print('cat yaht')
        for i in range(1,4):
            if dice[i] == dice[i+1]:
                points = 50
            else:
                points = 0
    if category in range(1,7):
        print('cat ones-sixes')
        points = dice.count(category)*category

    if category == 7:
        print('full house cat')
        if (dice.count(max(dice)) == 2 and dice.count(min(dice)) == 3) or (dice.count(max(dice)) == 3
                                    and dice.count(min(dice)) == 2):
            points = sum(dice)
        else:
            points = 0

    if category == 8:
        if dice.count(max(dice)) == 4 or dice.count(max(dice)) == 5 :
            points = max(dice)*4
        elif dice.count(min(dice)) == 4 or dice.count(min(dice)) == 5:
            points = min(dice)*4
        else:
            points = 0

    if category == 9:
        if [1,2,3,4,5] == sorted(dice):
            points = 30
        else:
            points = 0

    if category == 10:
        if [2,3,4,5,6] == sorted(dice):
            points = 30
        else:
            points = 0

    if category == 11:
        points = sum(dice)

    print(points)
    return points
