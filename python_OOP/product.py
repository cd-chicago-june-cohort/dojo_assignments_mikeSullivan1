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
    
    def display(self):
        print "Price: ", self.price, '\n',"Item Name: ", self.name, "\nWeight: ", self.weight, "\nBrand: ", self.brand, "\nCost: ", self.cost, "\nStatus: ", self.status, "\n",50 *'='
        return self
       
example= product(.75,"lacroix","12oz","soda", .50)
example.display()
print example.add_tax(.1)
example.display
example.sell()
example.return_item("open box")
example.display()
example.sell()
example.return_item("like new")
example.display()
example.sell()
example.return_item("defective")
example.display()
