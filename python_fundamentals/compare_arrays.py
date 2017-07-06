def compare_arrays(list_a, list_b):
    if len(list_a) is not len(list_b):
        return False
    for x in range(0,len(list_a)):
        if list_a[x] is not list_b[x]:
            return False
    return True

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if compare_arrays(list_one,list_two):
    print "The lists are the sames."
else:
    print "The lists are not the same."


'''
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]


'''