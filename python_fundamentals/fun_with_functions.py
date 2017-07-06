def odd_even():
    for i in range(1,2000): #setting range
        print i , 
        if i%2==0: #if divisible by 2
            print " is even"
        else:
            print " is odd"

def multiply(list,multiplier):
    y = [] # new list
    for x in list:
        y.append(x*multiplier) #adding to new list
    return y # retruning new list

def layered_multiples(arr):
    new_array = []
    for x in arr: #each num in list
        y = [] # temp array for sublist, reinitiate for each pass
        for size in range(0,x): # for each int in num
            y.append(1) # adding 1 to sub list
        new_array.append(y) # adding sublist to new array
    return new_array


odd_even()
a = [2,4,10,16]
b = multiply(a,5)
print b

print layered_multiples(multiply([2,4,5],3))