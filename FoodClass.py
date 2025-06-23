class Customer:
    
    def __init__(self, customerid, name, address, email, phone, member_status):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = member_status

    def getID(self):
        return self.customerid
    
    def getName(self):
        return self.name
    
    def getAddy(self):
        return self.address
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def isMember(self):
        return self.member_status


class Transaction:

    def __init__(self, date, item, cost, customerID):
        self.date = date
        self.item = item
        self.cost = cost
        self.customerID = customerID

    def getDate(self):
        return self.date
    
    def getItem(self):
        return self.item
    
    def getCost(self):
        return self.cost
    
    def getCustomerID(self):
        return self.customerID