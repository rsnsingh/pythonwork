import sys
a=int(input('enter a: '))
b=int(input('enter b '))
try:
    res=a/b
    print(res)
except:
    print('exception handled')
    print("Oh!!", sys.exc_info()[0],' has occured')
print('end of program')
