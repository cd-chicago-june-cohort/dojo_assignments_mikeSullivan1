import datetime

class Call(object):
    class_counter=1
    def __init__(self,name,phone,reason):
        self.id=Call.class_counter
        Call.class_counter+=1
        self.name=name
        self.phone=phone
        self.time=datetime.datetime.now()
        self.reason=reason

    def display(self):
        string = "\tID: {}\n\tCaller Name: {}\n\tPhone Number: {}\n\tTime Of Call: {}\n\tReason For Call: {}\n".format(self.id,self.name,self.phone,self.time,self.reason)
        string += '\t' + 50 *'-'
        print string
        return self

class Call_Center(object):
    def __init__(self):
        self.call_list = []
        self.queue_size =0
    
    def add_call(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self

    def remove_call(self):
        self.call_list.pop(0)
        self.queue_size -= 1
        return self
    
    def info(self):
        if self.queue_size == 0:
            print" There are no calls in the Queue"
            return self
        string = "Queue\n=====\nName\tPhone\n"
        for x in self.call_list:
            string += "{}\t{}\n".format(x.name,x.phone)
        string+= "There are {} call(s) in the queue.".format(self.queue_size)
        string += '\t' + 50 *'-'
        print string
        return self


call1 = Call("burt","911","to get to the other side")
call1.display()

call2 = Call("ernie","345-5678","cant find their books")
call2.display()

call3 = Call("moe","777-8968","to chat")
call3.display()

center1 = Call_Center()
center1.add_call(call1).info().remove_call().info()

center1.add_call(call2).info()
center1.add_call(call3).info()
