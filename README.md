# Coffee-Shop-Challenge

# **Coffee Shop Ordering System**

This is a simple python application patterning a coffee shop's coffees,customers and orders.It shows the core principles of object-oriented programming (OOP) like class relationships and data encapulation.

## **Instalatin**

GITHUB REPOSITORY: [coffee-shop-challenge](https://github.com/Richard3wasonga/coffee-shop-challenge)

1. Clone this repository:
   ```bash
   git clone https://github.com/Richard3wasonga/coffee-shop-challenge 
   ```

2. Navigate to the project directory:
  ```bash
  cd coffee-shop-challenge
  ```

3. Install dependencies and create virtual environment:
   ```bash
   pipenv install
   ```

4. Enter virtual environment:
   ```bash
   pipenv shell
   ```

---

## **File Overview**

This system consist of three main classes.

### **Customer.py**

This class takes a customer name and tracks all customer instances.

### **Customer Methods**

- `orders()`: Returns all orders placed by a customer.
- `coffees()`: Return unique list of coffee types the customer has ordered.
- `create_order(coffee, price)`: Create a new order for a specific customer.
- `total_spent()`: Return total amount spent by the customer across all orders.
- `most_aficionado(coffee)`: Class method to find the customer who spent the most on a given coffee.

```python
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

 
 ```

 ---

### **coffee.py**

This file takes a coffee type with a validated name and tracks all coffee instances.

### **Coffee Methods**

- `orders()`: Returns all orders of a specific coffee.
- `customers()`: Return all customers who ordered a specific coffee.
- `num_orders()`: Returns number of times a specific coffee was ordered.
- `average_price()`: Return average price at which a specific coffee was sold.

```python
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


```
---

### **order.py**

This file reperesent a purchase linking a customer,coffee, and price,tracks all orders,validates inputs and restrict price modification once an instance is created.

```python
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

    
```

---

## **How to use the system**

1. Create customers and coffees:
   ```python
   kylie = Customer("Kylie")
   latte = Coffee("Latte")
   ```
2. Create orders:
   ```python
   order1 = Order(kylie,latte, 3.5)
   ```

   or via customer method

   ```python
   kylie.create_order(latte,3.5)

   ```
3. Retrieve data:

   ```python
   print(kylie.orders())           # List of all Kylie’s orders
   print(latte.customers())        # Customers who ordered latte
   print(latte.num_orders())       # Number of latte orders
   print(latte.average_price())    # Average latte price
   print(Customer.most_aficionado(latte))  # Customer who spent most on latte
   print(Order.total_sales())      # Total revenue from all orders
   print(kylie.total_spent())      # Total spent by Kylie

   ```
---

## **Important Notes**

- **Price validation**: Ensures the price is a float between 1.0 abd 10.0.

- **Name Validation**: Customer and Coffee names are validated for type and length.

- **Instance Tracking**: Each class uses variables like `customer.all` to keep track of all instances for easy querying.

- **Circular Imports**: Avoided by importing classes **inside methods** instead of at the top of the file.

- **Why Use**`main.py`: All object creation is done `main.py` to **separate business logic from class definitions** and to **prevent circular import issues**.

---
## **Project Structure**

  ```css
  Coffee_Shop_Challenge/
  |__ customer.py
  |__coffee.py 
  |__order.py
  |__main.py
  |__README.md

  ```

## **Features Overview**

- Prevent duplicate data or invalid inputs

- Caluculate number and average price of order

- Identify customer who spend the most per coffee type

---

## **Authors**
- Richard Wasonga - [GitHub Profile](https://github.com/Richard3wasonga)

## **Contributors**
- Bob Oyier - [GitHub Profile](https://github.com/oyieroyier)

---

## **License**

This project is open-source and available under the MIT License.

