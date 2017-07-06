import math

def isPrime(some_num):
    for i in range(2,some_num):
        if some_num%i ==0: 
            return False #if any number between 2 and some num has no remainder, then it is not prime.
    return True

def isPerfectSquare(some_num):
    if round(math.sqrt(some_num)) == math.sqrt(some_num): #sqrt returns double. if the sqrt is perfect then xx.00 == xx (xx is rounded value) if the sqrt is not perfect xx.03 != to xx 
        return True
    return False

low = 100
high = 100000

for x in range(low, high):
    print x, 
    if isPrime(x):
        print "Foo" 
    if isPerfectSquare(x):
        print "Bar"
    if not isPrime(x) and not isPerfectSquare(x):
        print "FooBar"

