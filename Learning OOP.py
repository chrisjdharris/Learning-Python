#method example:
# random_string = "aaa"
# random_string.upper() <- .upper() is a METHOD

#Methods are functions inside classes!

class Item:
    #Class attributes
    pay_rate = 0.8 #The pay rate after 20% discount
    all = [] #List all instances of the class

    def __init__(self, name: str, price: float, quantity: int): #Constructor - this function is automatic
            
        #Run validations to the received arguments
        #Assert = #Check that what is happening matches expectations
            #If false, throws the error
        assert price >=0, f"Price {price} is not greater than zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!" 

        #Assign 'instance attributes' to self object
        print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self) #Add this instance to the 'all' list

    
    def calculate_total_price(self): #self is item1
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 100, 5) # __init__ automatically executed #'Phone' becomes the 2nd parameter in the init constructor
print("item1 total price: ",item1.calculate_total_price())

item2 = Item("Laptop", 1000, 3) #'Laptop becomes self.name
item2.has_touchscreen = False #Additional attributes can be added to individual instances
item2.quantity = 5 #Attributes can be updated
item2.pay_rate = 0.7 #Class-level attributes can be updated too!
print("item2 total price: ",item2.calculate_total_price())


print(Item.__dict__) #Magic attribute: shows all atributes at class-level
print(Item.pay_rate)
print(item1.__dict__) #Magic attribute: shows all atributes at instance-level
print(item1.pay_rate) #Looks at instance attributes, then if cannot be found looks at class attributes

item1.apply_discount()
print(item1.price)
item2.apply_discount()
print(item2.price)

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#List all instance names of class 'Item'
for instance in Item.all:
    print(instance.name)
