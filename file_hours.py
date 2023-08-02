filename=input("Enter the file name in which you want to read ? ")
input = open(filename)
for line in input:
    id, name, mon, tue, wed, thu, fri = line.split()

    # cumulative sum of this employee's hours
    hours = float(mon) + float(tue) + float(wed) + \
            float(thu) + float(fri)
    
    print(name, "ID", id, "worked", \
          format(hours, '0.2f'), "hours: ", format(hours/5, '0.2f'), "/ day")
