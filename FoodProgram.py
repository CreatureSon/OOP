import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

#First Customer - Danni Sellyar
#''' (<--remove Hashtag to run second customer)
customer = fc.Customer(570, "Danni Sellyar", 
                       "97 Mitchell Way Hewitt Texas 76712",
                       "dsellyarft@gmpg.org", 
                       "254-555-9362", False)
           

#Second Customer - Aubree Himsworth
'''
customer = fc.Customer(569, "Aubree Himsworth",
                       "1172 Moulton Hill Waco Texas 76710",
                       "ahimsworthfs@list-manage.com",
                       "254-555-2273", True)
#'''

print(f"Customer Name: {customer.getName()}")
print(f"Phone: {customer.getPhone()}")

sale_total = 0
discount = 0
for sale in dict.keys():

    # Create Transaction instance
    transaction = fc.Transaction(dict[sale][0], dict[sale][1], dict[sale][2], dict[sale][3])
    
    # Compare Transaction Customer ID to current Customer
    if transaction.getCustomerID() == customer.getID():
        print(f"Order Item: {transaction.getItem()}  Price: ${transaction.getCost():,.2f}")
        sale_total += transaction.getCost()
    
#Report Total Cost before discounts
print(f"Total Cost: ${sale_total:,.2f}")

# If Customer is a Member, apply discount
if customer.isMember():
    # 20% discount
    print(f"Member Discount: ${round(sale_total * 0.20, 2):,.2f}")
    sale_total -= round(sale_total * 0.20, 2)
    print(f"Total Cost after discount: ${sale_total:,.2f}")