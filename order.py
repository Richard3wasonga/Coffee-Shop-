from customer import Customer
from coffee import Coffee

class Order:

    all = []

    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.coffee = coffee
        self._set_price = False
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self,current_customer):
        if not isinstance(current_customer,Customer):
            raise TypeError("customer must be a Customer instance")
        self._customer = current_customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self,current_coffee):
        if not isinstance(current_coffee,Coffee):
            raise TypeError("coffee must be a Coffee instance")
        self._coffee = current_coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if self._set_price:
            raise AttributeError("Price cannot be changed.")
        if not isinstance(new_price,float):
            raise TypeError("Price must be a float.")
        if not(1.0 <= new_price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")

        self._price =new_price
        self._set_price = True



