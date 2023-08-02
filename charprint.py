print(' print the alphabets')
print('press 1 for uppercase')
print ('press 2 for lowercase')
c=eval(input('enter the choice :'))
if c==1:
    for i in range(65,91,1):
       print(chr(i),end=" ")
elif c==2:
    for i in range(97,123,1):
        print(chr(i),end=" ")
else:
    print('wrong choice')
