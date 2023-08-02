class A:
    def __init__(self):
        self.P=10
        self.__Q=20
    def gety(self):
        return (self.__Q)
ob1=A()
print(ob1.__Q)
