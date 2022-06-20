def primecheck(x):
 z=int(0)
 a=True
 
 for i in range(2,x):
    z=x%i;
  
    if z==0:
        a==True
        break
 if a:
    print("prime")
            
 else:
    print("not prime")
x=int(input("please enter a number for prime check"))
primecheck(x)
            
    