x=int(input("Please enter a number"))

for i in range(1,x+1):
    z=i%2
    if z==0:
        print(i,"even")
        
    if z!=0:
        print(i,"odd")
    
    