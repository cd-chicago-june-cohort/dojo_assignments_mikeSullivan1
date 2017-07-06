
def print_dict(dict):
    print "My name is", dict["name"]
    print "My age is", dict["age"]
    print "My country of birth is", dict["birthplace"]
    print "My favorite language is", dict["language"]

myDict = {}
myDict["name"]="Mike"
myDict["age"]=34
myDict["birthplace"]="USA"
myDict["language"]="Python"
print_dict(myDict)