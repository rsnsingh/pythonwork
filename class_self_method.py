class self_demo:
    def method_A(self):
        print('In method A')
        print(' got a call from A')
        self.method_B()
    def method_B(self):
        print(' In method_B calling method_A')
        
ob=self_demo()
ob.method_A()
        
