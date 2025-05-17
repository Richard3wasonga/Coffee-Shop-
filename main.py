from customer import Customer
from coffee import Coffee
from order import Order

kylie = Customer("Kylie")
beth = Customer("Beth")
sophie = Customer("Sophie")
diana = Customer("Diana")

latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")
mocha = Coffee("Mocha")

order1 = Order(kylie, latte, 3.5)
order2 = Order(beth, espresso, 2.0)
order3 = Order(sophie, cappuccino, 4.0)
order4 = Order(diana, latte, 3.5)
order5 = Order(kylie, mocha, 4.5)
order6 = Order(beth, latte, 3.5)

print(kylie.coffees())