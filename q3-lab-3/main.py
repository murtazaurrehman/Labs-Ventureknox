x=int(input("Please enter the first number"))
y=int(input("Please enter the second number"))
z=int(y*(-1))
if z==1:
    for i in range(x,y-1,-1):
        print(i)
        
elif z==-1:
    for i in range(x,y+1,1):
        print(i)
