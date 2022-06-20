print("Please enter the number of rows for your array")
r=int(input())
print("Please enter the number of collumns for your array")
c=int(input())
a=[]
for i in range(r):
    matrix=[]
    for j in range(c):
        matrix.append(int(input("Enter number for row: ")))
    a.append(matrix)
print(a)
trans = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

for i in trans:
   print(trans)