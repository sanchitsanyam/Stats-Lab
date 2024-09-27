import matplotlib.pyplot as plt
import math
import numpy as np


    
x=[3 , 3 , 4 , 5 , 6, 6, 7, 8, 8, 9]
y=[9, 5 , 12 ,9 , 14, 16, 22, 18, 24, 22]
n=len(x)
Sum_X=0
Sum_y=0
Sum_xy=0
Sum_x2=0
Sum_y2=0
i=0
n=len(x)
for i in range(n):
   Sum_X=Sum_X+x[i]
   Sum_y=Sum_y+y[i]
   Sum_xy=Sum_xy+x[i]*y[i]
   Sum_x2=Sum_x2+x[i]*x[i]
   Sum_y2=Sum_y2+y[i]*y[i]
mux=Sum_X/n
muy=Sum_y/n
a=(n*Sum_xy-Sum_X*Sum_y)/(n*Sum_x2-Sum_X*Sum_X)
b=(1/n)*(Sum_y-a*Sum_X)
   
Lxy= (float)(Sum_xy-(1/n)*(Sum_X)*(Sum_y))  
Lxx= (float)(Sum_x2-(1/n)*(Sum_X)*(Sum_X))
Lyy= (float)(Sum_y2-(1/n)*(Sum_y)*(Sum_y))
crr=(float)(Lxy)/(float)((math.sqrt(Lxx*Lyy)))
sx=math.sqrt(Lxx)
sy=math.sqrt(Lyy)
X= np.linspace(-5,5,100)
sx=math.sqrt(Lxx)
sy=math.sqrt(Lyy)
print("sx=",sx)
print("sy=",sy)
print("Ux =",mux)
print("Uy=",muy)
X1= np.linspace(-5,5,100)
t=crr*(sy/sx)
t2=(sy/(sx*crr))
Y1=(t)*X+muy-t*mux
Y2=(t2)*X+muy-t2*mux
Y3=a*X+b
print("Y =",t,"*X +",muy-(t)*mux)
print("X =",crr*(sx/sy),"*Y +",mux-(crr*(sx/sy))*muy)
print("Y =",a,"*X +",b)
plt.plot(X1,Y1 ,'-r',label='y')
plt.plot(X1,Y2 ,'-b',label='y')
plt.plot(X1,Y3 ,'-o',label='y')

plt.show()
