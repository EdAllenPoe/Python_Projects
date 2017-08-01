

import random

def scoresgrades():

    for x in range(10):

        score=random.randint(60,100)

        if score >89 and score <101:
            print "Score: ",score,": Your grade is A"
        elif score >79 and score< 90:
            print "Score: ",score,": Your grade is B"
        elif score >69 and score< 80:
            print "Score: ",score,": Your grade is C"
        elif score >59 and score < 70:
            print "Score: ",score,": Your grade is D"


scoresgrades()

print "End of program. Bye"
