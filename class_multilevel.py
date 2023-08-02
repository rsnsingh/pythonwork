class A:
    def Message1(self):
        print('I am in A')

class B(A):
    def Message2(self):
        print('I am in B')
        
class C(B):
    def Message3(self):
        print('I am in C')   

D1 = C()
D1.Message3()
D1.Message2()
D1.Message1()
