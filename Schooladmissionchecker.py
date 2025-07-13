print("Welcome to my school admission checker")
a = int(input("Please enter your age: "))

if a >= 5:
    b = input("Have you completed your pre-school? (yes/no): ")
    if b.lower() == "yes":
        print("You are eligible for admission.")
    else:
        print("You must complete pre-school first.")
else:
    print("You are too young for school.")
