import re

class Customer:

    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise TypeError("Name must be a string")
        if not re.match(r'^.{1,15}$', new_name):
            raise ValueError("Name must be between 1 and i5 characters.")
        self._name = new_name

