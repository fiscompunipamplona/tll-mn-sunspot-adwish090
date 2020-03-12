from numpy import linspace, sin
from pylab import plot,show
x= linspace (0,10,100)
print(x)
y= sin(x)
plot(x,y)
show ()

a=open("test.dat", "w")
for i in range(len(x)):
	a.write("%.2f %.2f\n" % (x[i],y[i]))
a.close()
