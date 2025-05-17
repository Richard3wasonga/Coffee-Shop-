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

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0
        return sum([order.price for order in orders]) / len(orders)



# COFFEE PSEDO CODE
# -----------------

# class Coffee
#      all_coffees = []

#      INIT(name):
#          IF name is not a string:
#               RAISE TypeError
#          IF name is shorter than 3 characters:
#              RAISE ValueError
#         SET internal name
#          ADD self to coffee.all_coffees


#      GET name:
#         RETURN internal name

#     DEF orders():
#           IMPORT order class
#          RETURN list of orders where order.coffee == self

#      DEF customers():
#           RETURN unique list of customers from self coffee's orders

#      DEF num_orders():
#           RETURN number of orders for this coffee

#     DEF average_price():
#          IF no orders:
#              RETURN 0
#          RETURN average of order prices for self coffee