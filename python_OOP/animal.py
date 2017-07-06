class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
    
    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -=5
        return self

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health+=5
        return self
    
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health=170

    def fly(self):
        self.health-=10
        return self
    
    def dragon_health(self):
        self.display_health()
        print "I am a Dragon"
        return self

bat = Animal("stevie")
bat.display_health()

wolf = Dog("Nerf")
wolf.display_health()
wolf.pet().display_health()

adragon = Dragon("Rhys")
adragon.dragon_health().fly().dragon_health()