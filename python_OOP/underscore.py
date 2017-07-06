class Underscore(object):
    
    def map(self,list,action):
        newlist=[]
        for x in list:
            newlist.append(action(x))
        return newlist
        
    def reduce(self,list,action,memo):
        for x in list:
            action(memo,x)
        return memo

    def find(self, list, action):
        for x in list:
            if action(x):
                return x
        return "undefined"

    def filter(self,list,action):
        newlist=[]
        for x in list:
            if action(x):
                newlist.append(x)
        if len(newlist):
            return newlist
        else:
            return "undefined"

    def reject(self,list,action):
        newlist=[]
        for x in list:
            if not action(x):
                newlist.append(x)
        if len(newlist):
            return newlist
        else:
            return "undefined"

# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print evens
# should return [2, 4, 6] after you finish implementing the code above

