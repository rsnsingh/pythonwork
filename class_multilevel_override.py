class A:
    def Message(self):
        print('I am in A')

class B(A):
    def Message(self):
        print('I am in B')
        super().Message()
        
        
class C(B):
    def Message(self):
        print('I am in C')   
        super().Message()
        

D1 = C()
D1.Message()

