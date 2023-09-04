import matplotlib.pyplot as pl
x=[2003,2007,2012,2018]
y=[200,500,600,1020]
z=[100,300,700,800]
pl.plot(x,y,'yellow',linestyle='dashed',marker='+',markeredgecolor='red',linewidth=3)
pl.plot(x,z,'purple',linestyle='solid',marker='>',markeredgecolor='orange',linewidth=8)
pl.xlabel('years')
pl.ylabel('shoes sale')
pl.title('sales of shoes every year')
pl.grid(True)
pl.show()