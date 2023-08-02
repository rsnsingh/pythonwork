class A:
    def Message(self):
        print('I am in A')

class B:
    def Message(self):
         print('I am in B')
        
class C(A,B):
    def Message(self):
        A.Message(self)
        B.Message(self)
        print('I am in C')   

D1 = C()
D1.Message()

