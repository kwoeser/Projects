###
# Karma Woeser
# CARDS MODULE
###

import random

def your_cards():
    x=random.randint(1,11)
    y=random.randint(1,11)
    print("Your 2 cards were {} and {}".format(x,y))
    equal_1=x +y
    print("The sum of your cards are",equal_1)
    

def player_cards():
    a=random.randint(1,11)
    b=random.randint(1,11)
    print("His 2 cards were {} and {}".format(a,b))
    equal_2=a +b
    print("The sum of his cards are",equal_2)

