def bin_search(data,key):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if (data[mid]==key):
            return mid
        elif key>data[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
data=[12,23,34,45,66,89]
print("Content of list are as :")
print(data)
key=eval(input("Enter the element to be searched? "))
loc=bin_search(data,key)
if(loc!=-1):
    print(key, " is found at position :  ", loc+1)
else:
    print(key, " is not found in the list ")


 








