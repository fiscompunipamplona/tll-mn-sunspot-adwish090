from pylab import plot,show,xlim,ylim,xlabel,ylabel
from numpy import linspace,sin,cos

x=linspace(0, 10, 100)
y=sin(x)
x1=linspace(0,10,100)
y1=cos(x)
plot(x,y, "k--")
ylim(-1.1,1.1)
xlim(0,9)
plot(x1,y1, "b--")
xlabel("radians")
ylabel("frecuence")
show()
