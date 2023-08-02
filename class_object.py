class complex1:
    real=0
    imag=0
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def printt(self,obj):
        print(' complex number is ', obj.real , '+', obj.imag,'i')
    def calculate(self,obj1,obj2):
        print('real (passed object)= ',obj1.real)
        print('imag (passed object)= ', obj1.imag)
        print('real (invoking object)= ',self.real)
        print('imag (invoking object)= ', self.imag)
        obj2.real=self.real+obj1.real
        obj2.imag=self.imag+obj1.imag
        printt(self,self)
        printt(self,obj1)
        printt(self,obj2)
      
obj1=complex1(10,20)
obj2=complex1(20,30)
obj3=complex1(0,0)
print(' addition of two complex numbers =', obj3.calculate(obj1,obj2))
