#create a line chart that will compect the sales oof two types of clothes that cloth1 and cloth 2 in gven four years.cloth 1 were represent by
#by blue color line and its cordinale points in the orm of circle of red coloorwhich cloth2 represent by  red color line and its cordinate points
#by + of blue color and its width is more than cloth 1. title will becloth 1 v/s cloth 2 an title x years and y be cloths.
#         years       cloth1         cloth 2
#         2003        2000            7000
#          2007        4000           3000
#          2012       7000            4000
#          2018        500              500
import matplotlib.pyplot as pl
x=[2003,2007,2012,2018]
y=[2000,4000,7000,500]
z=[7000,3000,4000,500]
pl.plot(x,y,'b' ,linestyle='dashed',marker='.',markeredgecolor='red')
pl.plot(x,z,"r",linestyle='solid',marker='+',markeredgecolor="blue")
pl.title('cloth1 v/s cloth2')

pl.xlabel('years')
pl.ylabel('cloths')
pl.grid(True)
pl.show()