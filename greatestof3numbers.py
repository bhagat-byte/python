print("Now enter 3 numbers and I will show the biggest number them.")
a = int(input("Enter number one "))
b = int(input("Enter number two "))
c = int(input("Enter number three "))
if a>b:
    if a>c:
        print ("The biggest number is "+str(a))
    else:
        print("The biggest number is "+str(c))
elif b>c:
    print("The biggest number is "+str(b))
else:
    print("The biggest number is "+str(c))