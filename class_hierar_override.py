class A:
    def Message(self):
        print('I am in A')

class B(A):
    def Message(self):
        super().Message()
        print('I am in B')

class C(A):
    def Message(self):
        super().Message()
        print('I am in C')
        
D1 = B()
D1.Message()

D2 = C()
D2.Message()
