n=eval(input('enter the value of N'))
sum=0
for i in range(1,n+1):
    print(i,end=" ")
    sum=sum+i
    i=i+1

print()
print('sum of', n, 'natural number is ',sum) 
