x= [['Name', 'HW1', 'HW2', 'HW3', 'HW4'], ['Steven', 8,7,9,4], 
['Lauren',7,9,8,6]]
y=[]
for list in x:
    for number in list:
        y.append(number)
name1=y[5]
name2=y[10]
print("Their names are :",name1,"and",name2)

for i in range(5):
    print(y[i],end=" ")
print('/n')   
for i in range(5,10):
    print(y[i],end=" ") 
print('/n')   
for i in range(10,15):
    print(y[i],end=" ")
    
sum1=y[6]+y[11]
sum2=y[7]+y[12]
sum3=y[8]+y[13]
sum4=y[9]+y[14]

sum1=sum1/2
sum2=sum2/2 
sum3=sum3/2
sum4=sum4/4 
print('/n')
print(sum1,sum2,sum3,sum4,end=' ')


av1=int(0)
av2=int(0)
for i in range (6,10):
    av1=av1+y[i]
for i in range (11,15):
    av2=av2+y[i]

av1=av1/4 
av2=av2/4 
print('/n')
print(av1,av2,end=' ')