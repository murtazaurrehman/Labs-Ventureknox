print("Please enter the number of collumns for your array")
r=int(input())
print("Please enter the number of rows for your array")
c=int(input())
a=[]
for i in range(r):
    matrix=[]
    for j in range(c):
        matrix.append(int(input("Enter number for row: ")))
    a.append(matrix)
print(a)
print("Please enter the number of collumns for your second array")
x=int(input())
print("Please enter the number of rows for your second array")
y=int(input())
b=[]
for i in range(x):
    ma=[]
    for j in range(y):
        ma.append(int(input("Enter number for row: ")))
    b.append(ma)
    
print(b)


if r==x and c==y:
    h=[]
    for i in range(x):
        m=[]
        for j in range(y):
            m.append(0)
        h.append(m) 
    for i in range(r):
        for j in range(len(a[0])):
            h[i][j]=a[i][j]+b[i][j]
        
    for i in h:
        print(i)
