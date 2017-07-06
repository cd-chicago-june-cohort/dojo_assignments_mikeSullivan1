'''def replace_string(long_string, old,new):
    return long_string.replace(old,new)


words = "It's thanksgiving day. It's my birthday,too!"
old_string = "day"
new_string = "month" 
print words   
print replace_string(words,old_string,new_string)


def minmax(some_list):
    some_list.sort()
    x=len(some_list) -1
    print "Min is " +str(some_list[0])+"."
    print "Max is " +str(some_list[x])+"."
    

minmax([2,54,-2,7,12,98])


def print_first_last(some_list):
    x=len(some_list) -1
    print str(some_list[0]), str(some_list[x])
    return (str(some_list[0]), str(some_list[x]))

print print_first_last (["hello",2,54,-2,7,12,98,"world"])

'''

def new_list(some_int_list):
    some_int_list.sort()
    print some_int_list
    half=len(some_int_list)/2
    new_int_list= [some_int_list[:len(some_int_list)/2]]
    i=half
    while i<len(some_int_list):
        new_int_list.append(some_int_list[i])
        i+=1
    print new_int_list




new_list([19,2,54,-2,7,12,98,32,10,-3,6])