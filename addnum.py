a=eval(input('enter the a:  '))
b=eval(input('enter the value of b:  '))
print(type(a))
print(type(b))
c= a+b

print('a= ',format(a,"<10.2f"), end=' ') # left justification 

print('b= ',format(b,">10.2f"), end=' ')  # right justification

print('c= ',format(c,"<10.2f"))
