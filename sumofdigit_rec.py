def sumofdigit(n):
    if n==0:
        return 0
    else:
        return (n%10+sumofdigit(int(n/10)))
print(sumofdigit(245))
