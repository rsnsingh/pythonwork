class Rectangle:
    __length=0;         #Attribute  length
    __breadth=0;        #Attribute  breadth
    print('length=', __length, 'breadth=', __breadth)
R1 = Rectangle ()     #Instance of a class
print('Initial values of Attribute')
print('Length   = ',R1.__length)      #Access attribute length    
print('Breadth  = ',R1.__breadth)     #Access attribute breadth
print('Area of Rectangle = ',R1.__length * R1.__breadth )
R1.length   =  20   #Assign value to attribute length
R1.breadth  =  30   #Assign  value to attribute breadth 
print('After reassigning the value of attributes')
print('Length = ',R1.__length )
print('Breadth = ',R1.__breadth ) 
print('Area of Rectangle is ',R1.__length * R1.__breadth) 
