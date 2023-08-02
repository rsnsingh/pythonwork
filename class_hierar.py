class A:
    def Message1(self):
        print('I am in A')

class B(A):
    def Message2(self):
        print('I am in B')

class C(A):
    def Message3(self):
        print('I am in C')
        
D1 = B()
D1.Message2()
D1.Message1()

D2 = C()
D2.Message3()
D2.Message1()
