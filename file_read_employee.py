inputFile = open ("employee.txt", "r")

print ("Reading from file employee.txt")
for line in inputFile:
    name,job,income = line.split(',')
    last,first = name.split()
    income = int(income)
    print("Name: %s, %s\t\tJob: %s\tIncome: $%.2f" 
             %(first,last,job,income))

print ("Completed reading of file employee.txt")
inputFile.close()
