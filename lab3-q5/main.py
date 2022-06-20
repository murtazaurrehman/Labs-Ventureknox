
x=int(input("enter a number to check if it is prime"))
z=int()
for i in range(2,x):
    z=int(x%i)
if z==0:
    print("The number is not prime")
elif z!=0:
    print("The number is  prime")

