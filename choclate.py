sum1 = 0
for x in range(0,7):
    print('Day: ',x+1)
    for y in range(0,5):
        print('Chocolate No: ',y+1)
        n = int(input('Enter the cost of chocolate:'))
        sum1 = sum1 + n;
print(' Bill to be paid = :',sum1)
