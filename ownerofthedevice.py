print("Welcome user! ")
o = str(input("Enter the name of the owner of this device "))
u = str(input("Enter the name of the user "))
if u==(""+o):
    print("You are the owner of the this device")
else:
    print("You are not the owner of this device. "+o+" is the owner of this device.")