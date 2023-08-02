inputOK = False
while (inputOK == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
    except ValueError:    # Can’t convert to a number
        print("Non-numeric type entered '%s'" %num)    
    else:   # All characters are part of a number
        inputOK = True
num = num * 2
print(num)
