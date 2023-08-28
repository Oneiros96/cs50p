class Jar:
    """
    capacity:
    maximum amount of cookies that fits in the Jar
    set by providing an positiv Int as an argument when creating the class instance

    size:
    amount of cookies in the jar

    depostit:
    deposit n cookies to the jar

    withdraw:
    withdraw n coockies from the jar
    """
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        str = "🍪"
        return str * self.size


    def deposit(self, n):
        self.size = self.size + n


    def withdraw(self, n):
        self.size = self.size - n


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("invalid capacity")




    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Over capacity Limit")
        if size < 0:
            raise ValueError("Not enogh cookies")
        self._size = size
