
x=int(input("Please enter the number of your guests"))
y=[]
for i in range(0,x):
    st=input("Please enter the names of your guests")
    y.append(st)

mean=int(x/2);

for i in range (mean,x-1):
    print(y[i])
    
    