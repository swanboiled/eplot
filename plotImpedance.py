#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
from matplotlib import style
     

#open file
f = open(sys.argv[1])
try:
    content = f.readlines( )
finally:
    f.close( )


#manipulate data    
num=int(content[15].split()[1])
print num
R=[]
I=[]
for line in range(19,19+num):
    R.append(float(content[line].split()[2]))
    I.append(-1*float(content[line].split()[3]))
print R,I
# plot
style.use('ggplot')
plt.scatter(R,I,c='g')
plt.title('Impedance Spectroscopy')
plt.xlabel('R')
plt.ylabel('I')
plt.legend()
plt.show()
