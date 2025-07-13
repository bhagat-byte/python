print("Welcome to my sum of even numbers program")
a = int(input("Enter a number I will tell the sum of even numbers until there "))
sum=0
for i in range(a):
    i=i+1
    if i%2==0:
#        print(""+str(i)) 
        sum=sum+i
print("The sum of all the even numbers until "+str(a)+" is "+str(sum))