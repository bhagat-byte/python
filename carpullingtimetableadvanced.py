print("I am going to tell the timetable of the Manthan coordination.")
a = input("Now enter the day you want to know about: ").lower()

if a == "saturday" or a == "sunday":
    print("It is a holiday!")
    quit()  # or exit()

b = input("Now enter what you want to know about — pickup or drop: ").lower()

if a == "monday":
    if b == "drop":
        print("The drop is Election")
    elif b == "pickup":
        print("The pickup is Sreenath")

elif a == "tuesday":
    if b == "drop":
        print("The drop is Abijit")
    elif b == "pickup":
        print("The pickup is Abijit")

elif a == "wednesday":
    if b == "drop":
        print("The drop is Kishore")
    elif b == "pickup":
        print("The pickup is Kishore")

elif a == "thursday":
    if b == "drop":
        print("The drop is Sreenath")
    elif b == "pickup":
        print("The pickup is Sreenath")

elif a == "friday":
    if b == "drop":
        print("The drop is Kishore")
    elif b == "pickup":
        print("The pickup is Election")

print("Have a happy day!")