from cmath import pi


class MyCircle:
    def __init__(self,x,y,radius):
        self.__x=x
        self.__y=y
        self.__radius=radius;
    def getx(self):
        return self.__x;
    def gety(self):
        return self.__y;
    def getradius(self):
        return self.__radius;
    def setx(self,x):
        self.__x=x;
    def sety(self,y):
        self.__y=y;
    def setx(self,radius):
        self.__radius=radius;
    def display(self):
        print("Radius=",self.getradius,"The centre is:",self.getx,self.gety);
    def area(self):
        c=2*self.getradius*pi;
        return c;
    def area(self):
        a=pi*(self.getradius**2)
        return a;
    def distance(self,point):
        x=self.getx()
        y=self.gety()
        x2=point.getx()
        y2=point.gety()
        z=float((((y2)-(y))**2)+(((x2)-(x))**2)**0.5)
        return z;
        
        
        
point=MyCircle(3,9,20)  
point1=MyCircle(9,0,18) 
final= point.distance(point1)
print(final)