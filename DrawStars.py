
# Draw Stars Function

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars():

    for stars in x:

        print "*" * stars

draw_stars()


#Draw Stars Function Part 2

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars_two():

    for stars in x:
        if type(stars)==int:
            print "*" * stars
        else:
            print stars[0]*len(stars)

draw_stars_two()
