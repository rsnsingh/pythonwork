class Circle:
    pi=0;
    radius=0
    def __init__(self,r): 
        self.pi = 3.14
        self.radius=r
    def calc_area(self):
        return self.pi*self.radius**2
C1=Circle(5)
C2=Circle(10)
print(' The area of Circle is ',C1.calc_area())
print(' The area of Circle is ', C2.calc_area())
