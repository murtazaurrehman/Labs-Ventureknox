x=int(input("Please enter the number of items"))
y=[]
sum1=0
mean=int()
for i in range(0,x):
    yx= int(input("Please enter the items"))
    y.append(yx)
    
    
for i in range(0,x):
    sum1=sum1 + y[i]
    mean=sum1/x


for i in range(x-1):
    for j in range(x-i-1):
    
    
        if y[i]>y[i+1]:
            temp=y[i]
            y[i]=y[i+1]
            y[i+1]=temp
print("The mean is",mean,"The highest number is",y[x-1],"The lowest number is",y[0])
print("The sorted numbers are",y)

