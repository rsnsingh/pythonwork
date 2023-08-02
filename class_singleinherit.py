class A:
    def Message1(self):
        print('I am in A')

class B(A):
    def Message2(self):
        print('I am in B')
        
D1 = B()
D1.Message1()  # inherited method
D1.Message2()  
