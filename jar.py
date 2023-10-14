class Jar:
    def __init__(self,capacity=12):
        self.capacity=capacity
        self.size=0
        if self.capacity < 0:
            raise ValueError("Capacity is 0")

    def __str__(self):
        return "🍪"*self.size

    def deposit(self,n):
        self.size+=n
        if self.size > self.capacity:
            raise ValueError("It Exceed Capacity")


    def withdraw(self,n):
        self.size-=n
        if self.size < 0:
            raise ValueError("Nothing is left")
