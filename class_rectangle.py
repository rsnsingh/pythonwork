class Rectangle:
    __length=10;         #Attribute  length ( private)
    __breadth=10;        #Attribute  breadth  (private)
    def area(self):
        print('Initial values of Attribute')
        print('Length   = ',__length)      #Access attribute length    
        print('Breadth  = ',self.__breadth)     #Access attribute breadth
        print('area=', self.__length*self.__breadth)
R1 = Rectangle ()     #Instance of a class
R1.area()


