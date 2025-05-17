import re

class Customer:

    all = []

    def __init__(self,name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise TypeError("Name must be a string")
        if not re.match(r'^.{1,15}$', new_name):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = new_name

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self,coffee,price):
        from order import Order
        return order(self,coffee,price)

 