def sum_till_n(n, x=0):
    return x if x == n else x + sum_till_n(n, x + 1)


print(sum_till_n(5))
