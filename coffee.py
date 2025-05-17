import re

class Coffee:

    all = []

    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if not re.match(r'^.{3,}$', name):
            raise ValueError("Name must be above 3 characters")
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self] 

    def customers(self):
        return list({order.customer for order in self.orders()})

