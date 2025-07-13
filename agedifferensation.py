age = int(input("Enter your age: "))

if age <= 2:
    print("You are a baby.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 50:
    print("You are an adult.")
elif age <= 100:
    print("You are an old person.")
else:
    print("You are dead.")
