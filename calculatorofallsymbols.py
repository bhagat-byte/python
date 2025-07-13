print("Welcome to my calculator")
s = str(input("Now enter a symbol you want to use.+,-,*,/ "))
a = int(input("Now enter number 1 "))
b = int(input("Now enter number 2 "))
if s==("+"):
    c = a+b
    print("The sum of both numbers is "+str(c))
if s==("-"):
    c = a-b
    print("The answer of this subtraction problem is "+str(c))
if s==("*"):
    c = a*b
    print("The product of this multiplication problem is "+str(c))
if s==("/"):
    c = a/b
    print("The answer for this division problem is "+str(c))