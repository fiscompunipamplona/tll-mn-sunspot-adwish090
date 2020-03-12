from numpy import loadtxt,zeros
from pylab import plot,show,xlim,ylim,xlabel,ylabel
a=loadtxt("sunspots.txt",float)
xlabel("meses")
ylabel("numero de manchas")
xlim(0,1000)
ylim(0,250)
r=5
A=zeros([1000],float)
b=0
cons=(1/((2*r)+1))
for m in range(5,1001):
	for i in range(-r,r):
		sumy=(a[m+i,1])
		b=b+sumy
		c=cons+b
plot(a[:,0],c)
show()
