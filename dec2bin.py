dectobin={'0':'0000', '1':'0001',  '2':'0010',  '3':'0011',  '4':'0100',  '5':'0101',  '6':'0110',  '7':'0111','8':'1000','9':'1001'}
n=input('enter decimal number: ')
bin=' '
for i in n:
    print('decimal digit',i, end=" ")
    print('binary number', dectobin[i])
    bin=bin + dectobin[i]
print('decimal number is : ', n , ' binary equivalent is: ' ,bin)
