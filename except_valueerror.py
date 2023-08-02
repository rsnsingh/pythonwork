import sys
while True:
    try:
        x=int(input('enter the number : '))
        break
    except ValueError:
        print('OOps !  That was no valid number.. Try again')
        
