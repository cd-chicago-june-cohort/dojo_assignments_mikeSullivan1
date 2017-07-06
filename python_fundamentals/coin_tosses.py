import random

def flip(): 
    return random.randint(0,1) #False is tails; True is Heads


coinTosses = 5000
heads = 0
tails = 0
for x in range(0,coinTosses):
    print "Attempt #%d:Throwing a coin... It's a " % x,
    thisFlip = flip()
    if thisFlip:
        heads += 1
        print "head",
    else:
        tails += 1
        print "tail",
    print "! ... Got %d head(s) and %d tail(s) so far" % (heads,tails)
