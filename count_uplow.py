s=input('enter the sentence in upercase and lower case')
count=len(s)
countup=0
countlower=0
for i in s:
    if (i.isupper()):
        countup=countup+1
    else:
        countlower=countlower+1
print(countup)
print(countlower)
