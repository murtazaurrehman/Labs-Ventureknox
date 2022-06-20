x= ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 
27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
string=[]
integer=[]
floot=[]
for i in range(11):
    if type(x)==str:
      for j in range(11-i):
        st=x[i];
        string.append(st)
    
    elif type(x)!=str:
        for j in range(11-i):
            st=x[i]
            floot.append(st)
        
print(string,floot)
    

        
        
        
