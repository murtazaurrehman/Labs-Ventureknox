names = [ "Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", 
"Alex","Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
"Aaron", "Kate" ] 
times = [341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299, 
343, 317, 265]
x=(max(times))
y=times.index(x)
print("The fatest runner is:",x,names[y],"The second fatest runner is:",times[y-1],names[y-1])
dum1=0
for i in range (16):
    dum1=dum1 +times[i]
dum1=dum1/16
print(dum1)
for i in range(16):
    if times[i]>dum1:
        print(names[i],times[i])
