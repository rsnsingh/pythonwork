try:
    a=int(input('enter the value of a: '))
    b=int(input('enter the value of b: '))
    try:
        result=a/b
        print('result is: ', result)
    except:
        print('Exception handled')
except:
    print(' Invalid Input')
print('end of program')
