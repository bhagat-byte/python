country = input("Enter your country name? ")
age = int(input("Enter your age ? "))
if country=="India":
    if age>=18:
        print  ("You are elegible to vote in India")
    if age<18:
        print  ("You are not elegible to vote in India")
else:
        print  ("check the laws in "+ country)