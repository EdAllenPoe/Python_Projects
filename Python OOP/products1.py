class Product():
    def  __init__(self,itemname,price,weight,brand):
        self.status = "for sale"
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.cost = 0
        self.status = "for sale"
        self.tax=1.10

    def sell(self,sell):
        if (sell=="sold"):
            self.status = "sold"
            self.price=0
            self.cost=0
        else:
            self.price=self.price
        return self

    def Tax(self):
        self.cost=self.price*self.tax
        return self

    def Returned(self,returned):
        if (returned == "defective"):
            self.status = "defective"
            self.price = 0
        elif (returned == "in box"):
            self.staus = "for sale"
            self.price=self.price*.8
        else:
            self.price=self.price
        return self

    def displayinfo(self):
        print "Item name: ",self.itemname
        print "Price: $",str(self.price)
        print "Weight: " + str(self.weight) +"lbs"
        print "Brand: ",self.brand
        print "Cost: $",str(self.cost)
        print "Status: ",self.status
        return self

chairs=Product("Chairs",10,12,"Chairs-r-us").Returned("no").Tax().sell("sold")
chairs.displayinfo()

pants=Product("Pants",10,12,"Pants-r-us").Returned("in box").Tax().sell("for sale")
pants.displayinfo()

stuff=Product("Stuff",10,12,"Stuffs-r-us").Returned("spankin new").Tax().sell("for sale")
stuff.displayinfo()
