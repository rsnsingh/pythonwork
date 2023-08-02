s1=eval(input('enter the marks of subject 1'))
s2=eval(input('enter the marks of subject 2'))
s3=eval(input('enter the marks of subject 3'))
s4=eval(input('enter the marks of subject 4'))
s5=eval(input('enter the marks of subject 5'))
sum=(s1+s2+s3+s4+s5)/float(5)
print('percentage of marks',format(sum,"10.2f"))
if sum>=90:
    print('distinction')
elif sum>=80:
    print('first class')
elif sum>=70:
    print('second class')
elif sum>=60:
    print('pass')
else:
    print('fail')        
        
