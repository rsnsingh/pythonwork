def bin_to_dec(num):
    l=len(num)
    p=0
    z=0
    num=num[:: -1]
    for i in num:
        z=z+int(i)*(2**p)
        p=p+1

    print('Decimal equivalent is :->', z)
s=input('Enter the binary number:-> ')
bin_to_dec(s)
