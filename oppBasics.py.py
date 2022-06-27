from re import X
from tkinter import Y


class MyPoint:
    def __init__(self):
            
        self.__x=0
        self.__y=0
    
    def __init__(self,x,y):
            
        self.__x=x
        self.__y=y
       
    def setx (self,x):
        self.__x=x;

    def sety (self,y):
        self.__y=y;
        
    def getx (self):
        return self.__x;
    
    def gety(self):
        return self.__y;
    
    
    def somepoint(self):
        print("(",self.getx(),self.gety(),")")

    def another(self,r,t):
        return r,t;
    
        
    
    def distance(self, point):
        x=float(self.getx())
        y=float(self.gety())
        
        x2=float(point_1.getx())
        y2=float(point_1.gety())
        z=float((((y2)-(y))**2)+(((x2)-(x))**2)**0.5)
        print(z)
                


point_1 = MyPoint(2,5)
point_2 = MyPoint(9,6)
print(point_1.getx(),point_2.gety())
(point_1.distance(point_2) )     
# print(newdistance)  