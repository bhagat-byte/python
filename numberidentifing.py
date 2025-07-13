print("Welcome to my number identifing program")
import random
while True:
    a = random.randint(1,10)
    b = int(input("Now guess the number, between 1-10 "))
    if a==b:
        print("Congratulations! you have guessed the correct number.")
        break
    else:
        print("Good try, but you guessed it wrong. The correct number was, "+str(a))