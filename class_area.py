import math
class Circle:
    def calc_area(self,radius):
        print('radius= ', radius)
        return math.pi*radius**2
C1=Circle()
print(' The area of Circle is ',C1.calc_area(5))
