print "x", #comma allows for no carriage return
for y in range (1,14): #nested loop Y is the multiplicand for the rows(the verticals on the left)
    if y is not 1:
        print y-1,
        for x in range(1,13):#nested loop X is the multiplicand for the columns(the laterals on the top)

            print "  "+str(x*(y-1)), # y-1 for headers(range is to 14)
    else: # this entire else condition is for the headers
        for x in range(1,13):
            print "  "+str(x*y), # printing the multipied value
    print '' # carriage return at the end of the inner loop



"""hard coding the headers wouldve simplified the algorithm significantly I will do that here.
"""

print "+=" * 25 
print " This is another way thats more readable/elegant despite the hard coded headers"
print "+=" * 25 


print "x   1   2   3   4   5   6   7   8   9   10   11   12"
for y in range (1,13):
    print y,
    for x in range(1,13):
        print "  "+str(x*y),
    print ''