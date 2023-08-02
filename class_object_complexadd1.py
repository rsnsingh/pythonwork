class complex1:    #  real+imag i
    real=0
    imag=0
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def calculate(self,obj1,obj2):
        print(' complex number1 is ', obj1.real , '+', obj1.imag,'i')
        print(' complex number2  is ', obj2.real , '+', obj2.imag,'i')
        self.real=obj1.real+obj2.real
        self.imag=obj1.imag+obj2.imag
              
obj1=complex1(10,20)
obj2=complex1(20,30)
obj3=complex1(0,0)
obj3.calculate(obj1,obj2)
print(' addition of two complex numbers is= ', obj3.real , '+', obj3.imag,'i')
