class Circle:
    pi=0;
    radius=0
    def __init__(self): 
        self.pi = 3.14
        self.radius=5
    def calc_area(self):
        return self.pi*self.radius**2
C1=Circle()
C2=Circle()
print(' The area of Circle is ',C1.calc_area())
print(' The area of Circle is ', C2.calc_area())

