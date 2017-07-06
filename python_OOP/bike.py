class bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "This bike costs", self.price
        print "This bike can go", self.max_speed
        print "This bike has been ridden", self.miles
        return self
    def ride(self):
        print "RYDIN'"
        self.miles +=10
        return self
    def reverse(self):
        print "Rolling backwards"
        if self.miles>=5:
            self.miles -=5
        else:
            self.miles=0
        return self


bike1=bike(200,"25mph")
print " - " * 15
bike1.ride().ride().ride().reverse().displayinfo()

bike2=bike(8000,"40mph")
print " - " * 15
bike2.ride().ride().reverse().reverse().displayinfo()

bike3=bike(24,"15mph")
print " - " * 15
bike3.reverse().reverse().reverse().displayinfo()