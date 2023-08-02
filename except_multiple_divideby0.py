import sys
try:
    a=int(input('enter the value of a: '))
    b=int(input('enter the value of b: '))
    result=a/b
    print('result is: ', result)
except ValueError:
    print(' Invalid Input')
except ZeroDivisionError:
    print('Exception handled')
print('end of program')
