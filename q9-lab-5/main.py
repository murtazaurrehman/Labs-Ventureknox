x=["Karachi Kings vs Lahore Qalandars","Karachi Kings vs Peshawar Zalmi",
"Karachi Kings vs Multan Sultans",
"Karachi Kings vs Islamabad United",
"Karachi Kings vs Quetta Gladiators",
"Lahore Qalandars vs Peshawar Zalmi",
"Lahore Qalandars vs Multan Sultans",
"Lahore Qalandars vs Islamabad United",
"Lahore Qalandars vs Quetta Gladiators",
"Peshawar Zalmi vs Multan Sultans",
"Peshawar Zalmi vs Islamabad United",
"Peshawar Zalmi vs Quetta Gladiators", 
"Multan Sultans vs Islamabad United",
"Multan Sultans vs Quetta Gladiators", 
"Islamabad United vs Quetta Gladiators",]
y=[]
import random

for i in range(14):
    u=random.choice(x)
    y.append(u)
    v=x.index(u)
    del x[v]
print(y,x)