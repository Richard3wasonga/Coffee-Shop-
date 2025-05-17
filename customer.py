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

    @classmethod
    def most_aficionado(cls,coffee):
        maximum_spent = 0
        best_customer = None

        for customer in cls.all:
            orders_of_coffee = [order for order in customer.orders() if order.coffee == coffee]

            total_spent = sum(order.price for order in orders_of_coffee)

            if total_spent > maximum_spent:
                maximum_spent = total_spent
                best_customer = customer

        return best_customer


# CUSTOMER PSEDO CODE
#  -------------------

#class Customer:
#     all_customers = []

#     INIT(name):
#         VALIDATE name is string, 1-15 characters
#         SET internal name
#         ADD self to customer.all_customers

#     GET name:
#         RETURN internal name

#     SET name(new_name):
#         VALIDATE type and length
#         SET internal name

#     DEF orders():
#         IMPORT order
#         RETURN list of orders where order.customer == self

#     DEF create_order(coffee, price):
#          IMPORT order
#          RETURN new order with self,coffee, price

#     CLASS METHOD most_aficionado(coffee):
#         FOR each customer:
#              CALUCULATE total spent on given coffee
#         RETURN customer who spent the most

 