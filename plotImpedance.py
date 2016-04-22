#!/usr/bin/python
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import style
     
def getFromFile(f):
    f = open(f)
    try:
        content = f.readlines( )
    finally:
        f.close( )
    num=int(content[15].split()[1])
    F=[]
    R=[]
    I=[]
    for line in range(19,19+num):
        F.append(float(content[line].split()[1]))
        R.append(float(content[line].split()[2]))
        I.append(-1*float(content[line].split()[3]))
    return [F,R,I] 
def save(a,f):
   f = open(f,'w')
   for row in a:
       for line in row:
           f.write(str(line))
           f.write('\t')
       f.write('\n')
   f.close()
        


#Colors
color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

# plot

files = sys.argv[1:]
i=0
for f in files:
    O=getFromFile(f)    
    save(np.transpose(O),'cleaned-'+f)
    plt.scatter(O[1],O[2],label= f,color=color_sequence[i])
    i+=1
plt.title('Impedance Spectroscopy')
plt.xlabel('R')
plt.ylabel('I')
plt.legend()
plt.show()
