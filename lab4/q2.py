import matplotlib.pyplot as plt
import math
 
    
x=[12.5 , 5.0 , 3.0 , 5.0 , 6.5, 6.0,4.0 ,7.0, 5.5, 4.0]
y=[10, 26 , 41 ,29 , 27, 19, 18, 20, 28, 33]

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
   
Lxy= (float)(Sum_xy-(1/n)*(Sum_X)*(Sum_y))  
Lxx= (float)(Sum_x2-(1/n)*(Sum_X)*(Sum_X))
Lyy= (float)(Sum_y2-(1/n)*(Sum_y)*(Sum_y))
crr=(float)(Lxy)/(float)((math.sqrt(Lxx*Lyy)))


print ('{0:0.6f}'.format(crr)) 
plt.scatter(x, y, c="blue")
plt.show()
