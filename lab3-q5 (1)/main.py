n = int(input("Enter a number to check if it is perfect "))
x = 0
for i in range(1, n):
    if(n % i == 0):
        x = x + i
if (x == n):
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")