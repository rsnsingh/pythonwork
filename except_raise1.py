class InvalidRange(Exception):
    pass
try:
    print('enter the marks')
    marks=int(input())
    if marks<0 or marks>100:
       raise InvalidRange
except InvalidRange:
   print('Input out of range')
except ValueError:
    print('Invalid Input')
