print("Welcome to my fizzbuzz program.")
a = int(input("Now enter a number for my fizzbuzz program to work "))
b = 0
for i in range(a):
    b=i+1
    if b%5==0 and b%3==0:
        print("fizzbuzz")
    elif b%3==0:
        print("fizz")
    elif b%5==0:
        print("buzz")
    
    if b%5!=0 and b%3!=0:
        print(""+str(b))