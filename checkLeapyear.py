year = int(input("Enter an year: "))
#print (year%4)

if year%4==0:
    if year%100==0:
        if year%400==0:
            print ("This year is a leap year")
        else: print ("This year is not a leap year")
    else: print ("This year is a leap year")
else: print("This is not a leap year")