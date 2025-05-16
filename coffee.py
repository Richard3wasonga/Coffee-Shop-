class Coffee:

    def __init__(self,name):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if not re.match(r'^.{3,}$', name):
            raise ValueError("Name must be above 3 characters")
        self._name = name

    @property
    def name(self):
        return self._name

   