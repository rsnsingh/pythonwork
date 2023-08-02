class DestructorDemo:
          
    def __del__(self):    # destructor
        print('Destructor executed...')
   def __init__(self):    # constructor
        print('Welcome to Python')
        
ob1=DestructorDemo()    # __init__ is called here
ob2=DestructorDemo()
ob3=DestructorDemo()
print(' Id of ob1 = ', id(ob1))
print(' Id of ob2 = ', id(ob2))
print(' Id of ob3 = ', id(ob3))
del ob1    # __del__ will be called
del ob2
del ob3

# destructor is called thrice why????
