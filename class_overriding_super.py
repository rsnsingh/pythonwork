class A:
    def Message(self):
        print('I am in Super class A')

class B(A):
    def Message(self):
        super().Message()  # call to base class method
        print('I am in Sub class B')
        
D1 = B()
D1.Message()  

