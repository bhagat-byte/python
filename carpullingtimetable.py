print("I am going to tell the timetable of the Manthan coordination.")
a = input("Now enter the day you want to know about: ").lower()

if a == "monday":
    print("The drop is Election")
    print("The pickup is Sreenath")
elif a == "tuesday":
    print("The drop is Abijit")
    print("The pickup is Abijit")
elif a == "wednesday":
    print("The drop is Kishore")
    print("The pickup is Kishore")
elif a == "thursday":
    print("The drop is Sreenath")
    print("The pickup is Sreenath")
elif a == "friday":
    print("The drop is Kishore")
    print("The pickup is Election")
elif a == "saturday" or a == "sunday":
    print("It is a holiday!")
else:
    print("Invalid day entered.")
