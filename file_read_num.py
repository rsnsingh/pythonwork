'''fp=open('sd2.txt','r')
num=fp.read()
print(num)
print(type(num))'''

fp=open('sd2.txt','r')
num=int(fp.readline())
print(num)
sum=0
print('The', num,' numbers are present in the file which are as follows:')
for i in range(num):
    num1=int(fp.readline())
    print(num1)
    sum+=num1
print('sum of all numbers (except first ):')
print(sum)

