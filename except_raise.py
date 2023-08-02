try:
    print('enter the marks')
    marks=int(input())
    if marks<0 or marks>100:
        raise ValueError
except ValueError:
    print('Input out of range')
