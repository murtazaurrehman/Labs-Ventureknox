x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=int(input("Enter the jump number"))


if x>y:
    for i in range(x,y+1,-z):
        print(i)
elif x<y:
      for i in range(x,y+1,z):
        print(i)
    
    
