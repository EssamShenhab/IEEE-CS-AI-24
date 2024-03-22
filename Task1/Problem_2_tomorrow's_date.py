day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
while day <= 31 and month <=12:
    if day == 31 and month % 2 != 0:
        day = 1 
        month += 1
    elif day == 30 and ( month % 2 == 0):
        day = 1 
        month += 1
    elif day == 28 and month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            day += 1
        else:
            day = 1 
            month += 1
    else:
        day += 1
    
    if month == 13:
        month = 1
        year += 1
        
    print("Day:", day, "Month:", month, "Year:", year)
    break
        
else:
    print("Invalid input")