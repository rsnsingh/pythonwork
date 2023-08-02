class A:
    def Message(self):
        print('I am in A')

class B(A):
    def Message(self):
        #super().Message()
        print('I am in B')
        
D1 = B()
D1.Message()  

