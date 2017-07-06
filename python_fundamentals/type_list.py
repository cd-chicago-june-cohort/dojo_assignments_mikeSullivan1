from numbers import Number

def list_analyze(some_list):
    hasInt=False
    hasString=False
    sum=0;
    just_strings = ''
    for x in some_list:
        if isinstance(x,Number):
            sum+=x
            hasInt=True
        elif isinstance(x,basestring):
            just_strings+=x+" "
            hasString=True
        else:            
            continue    
    if hasInt==True and hasString == True:
        print "The array you entered is of mixed type"
    elif hasInt==True:
        print "The array you entered is of integer type"
    elif hasString==True:
        print "The array you entered is of string type"
    print "String: %s" % just_strings
    print "Sum:", sum
    print '=' *50


l = ['magical unicorns',19,'hello',98.98,'world']
m = [2,3,1,7,4,12]
n = ['magical','unicorns']

list_analyze(l)
list_analyze(m)
list_analyze(n)
