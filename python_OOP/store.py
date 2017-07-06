class product(object):
    def __init__(self,price,name,weight,brand,cost):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        print self.name,"was sold\n",50 *'='
        return self
    
    def add_tax(self,rate):
        return float(self.price) * (1.0+rate)
    
    def return_item(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            print self.name,"is defective and was returned.\n",50 *'='
            return self
        elif reason =="like new":
            self.status = "for sale"                
            print self.name,"is back in stock.\n",50 *'='
            return self
        elif reason == "open box":
            self.status = "for sale"
            self.price = .8 * self.price
            print "Open box", self.name,"is discounted and for sale.\n",50 *'='
            return self
    
    def __str__(self):
        string = "\tPrice: {}\n\tItem Name: {}\n\tWeight: {}\n\tBrand: {}\n\tCost: {}\n\tStatus: {}\n".format(self.price,self.name,self.weight,self.brand,self.cost,self.status)
        string += '\t' + 20 *'-'
        return string

class store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []
    
    def add_product(self,name):
        self.products.append(name)
        return self
    
    def __str__(self):
        string = "Location: {}\nOwner:{}\nProducts:\n".format(self.location,self.owner)
        counter =1
        for item in self.products:
            string += '\tProduct #{}:\n{}\n'.format(counter,item)
        return string
example= product(.75,"lacroix","12oz","soda", .50)
#print example

exstore=store("western","my boy roy")
exstore.add_product(example)
print exstore

