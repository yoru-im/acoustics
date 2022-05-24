# -*- coding: utf-8 -*-


import numpy as np
from matplotlib import pylab as plt

a0 = 1 
b0 = 0    
fs = 128
f00 = 150  
sec = 1   
value0=[]

a1 = 1
b1 = 0
f01 = 153
value1 = []


#サイン波を生成
for n in np.arange(fs * sec):
    s = a0 * np.sin((2.0 * np.pi * f00 * n / fs) + b0) + \
        a1 * np.sin((2.0 * np.pi * f01 * n / fs) + b1)
    value0.append(s)   

t = np.arange(0, len(value0))/fs

np.savetxt('sin.csv', [t,value0] ,fmt='%.5f',delimiter=',')

plt.plot(t,value0)
plt.title('150Hz,153Hz.sin curve')
plt.xlabel('time')
plt.ylabel('sin()')
plt.xlim([0,1])
plt.show()