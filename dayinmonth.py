month=eval(input('Enter the month in digit: '))
if month==2:
    print('Number of days in this month are: ',28)
elif month in (1,3,5,7,8,10,12):
    print('Number of days in this month are: ',31)
elif month in (2,4,6,9,11):
    print('Number of days in this month are: ',30)
else:
    print('invalid month')
    
