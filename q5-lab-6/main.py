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
# multiple1= [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]
# x=[]
# x.append(multiple1)
# print(a,x)
import numpy as np
blank=np.zeros((r,y))
#  blank.fill(0)
# for i in range(r):
#     kk=[]
#     for j in range(y):
#         kk.append(int(0))
#     blank.append(kk)
# blank2=np.matrix(blank)
# blank2.fill(0)
for i in range(len(a)):
   for j in range(len(b[0])):
       for k in range(len(b)):
           blank[i][j] += a[i][k] * b[k][j]
print(blank)