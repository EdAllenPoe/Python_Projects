class Call(object):
    def __init__(self,unique_id,name,phone,time,reason):
        self.unique_id=0
        self.name=name
        self.phone=phone
        self.time=time
        self.reason=reason
    def info(self):
        self.unique_id+=1
        print "User# : ",self.unique_id
        print "Name: ",self.name
        print "Phone # ",self.phone
        print "Call Time: ",self.time
        print "Reason for call: ", self.reason

patient1=Call(1,"Dracula","888.555.1212","8 o'Clock", "blood transfusion")
patient1.info()


class CallCenter(object):

    def __init__(self,name,phone):
        self.calls=[]
        self.queue=0
        self.name=name
        self.phone=phone
    def add(self):
        self.queue+=1
        self.calls.append (self.name)
        self.calls.append (self.phone)
        print self.calls
        # print type(self.calls)
        # print len(self.calls)
        return self

    def remove(self):
        return self

    def info(self):
        print "Name: ",self.name
        print "Phone # ",self.phone

    def info(self):
        x=0
        print "Que Length: ",self.queue
        # print "Name: ",self.calls(self.queue-1)(0)
        # print "Phone: ",self.calls(self.queue-1)(1)
        for info in self.calls:
            x+=1
            if x==1:
                print "Name:",info

            else:
                print "Number",info

patient2=CallCenter("Casper","666.666.1313").add()
patient2.info()
