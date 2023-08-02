L=[-1,10,-45,23,34]
sumneg=0
sumpos=0
avgg=0
summ=0
print (L)
print("Numbers are :")
for i in range(0,len(L)):
    if L[i]<0:
        sumneg+=L[i]
        summ+=L[i]
        print(L[i], end=" ")
    else:
        sumpos+=L[i]
        summ+=L[i]
        print(L[i], end=" ")
print("\nsum of negative numbers: \t", sumneg)
print("sum of positive numbers: \t", sumpos)
avgg=summ/len(L)
print("average of numbers: ", avgg)
print(" List of numbers which are greater than average")
for i in range(0,len(L)):
    if L[i]>avgg:
        print(L[i], end=" ")




        
        
