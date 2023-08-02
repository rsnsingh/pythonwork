import math
class Circle:
    def calc_area(self,length,breadth):
        print('length= ', length)
        print('breadth= ', breadth)
        return length*breadth
C1=Circle()
print(' The area of rectangle is ',C1.calc_area(4,5))
