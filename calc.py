import math
print("Welcome to Arithmetic calulator")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Adition")
print("Subsraction")
print("Multiple")
print("Division")
print("mod")
print("square ")
print("-----------------------------------------------")
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a**b
User_choice=input("Enter a your choice: ")
if User_choice=="Adition":
    print("Addition",c)
elif User_choice=="sunraction":
    print("subraction",d)
elif User_choice=="Multiple":
    print("multiple",e)
elif User_choice=="division":
    print("division",f)
elif User_choice=="mode":
    print("mode",g)
elif User_choice=="square":
    print("square",h)
else:
    ("Your choice is un available")

