
# self is used to differentiate between instance and local variable.
#e.g x displays the value of local variable and self.x displays the value of instance variable

class prac:
    x=5  # instance attribute /parameter
    def display(self,x):
        x=30
        print('value of local variable x is = ', x)
        print('value of instance variable x is = ', self.x)
    
ob=prac()
ob.display(50)
        
