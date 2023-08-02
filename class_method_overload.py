class DemoOverload:   # method overloading
    result=0
    def add(self, instanceOf=None, *args):
        if instanceOf=='int':
            self.result=0
        if instanceOf=='str':
            self.result=' '
        for i in args:
            self.result=self.result+i
        return self.result
D1=DemoOverload()

#print(D1.add('int',10,20,30))
#print(D1.add(30))        # output????
print(D1.add(10))     #output???? 
print(D1.add('str', 'India ','is ','Great'))
      
      
            
            
