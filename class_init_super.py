class BaseDemo:
    a=0
    b=0
    c=0
    def __init__(self,A,B,C):
        self.a=A
        self.b=B
        self.c=C
    def display(self):
        print( self.a, self.b, self.c,end=' ')

class DerivedDemo(BaseDemo):
    d=0
    def __init__(self,A,B,C,D):
        self.d=D
        super().__init__(A,B,C)
    def display(self):
        super().display()
        print(self.d)

#B=BaseDemo(10,20,30)
#print('content of Base class: ')
#B.display()

P=DerivedDemo(10,20,30,40)
print('content of derived class: ')
P.display()
