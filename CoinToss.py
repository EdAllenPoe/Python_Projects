import random

def cointoss():

    heads=0
    tails=0

    for coins in range (5000):

        toss=random.randint(1,2)

        if toss==1:
            heads=heads+1
            x="head"

        else:
            tails=tails + 1
            x="tail"

        print"Attempt #",coins,": Throwing a coin... It's a",x, "! ... Got",heads," head(s) so far and",tails," tail(s) so far"

cointoss()
