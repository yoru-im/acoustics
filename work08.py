# -*- coding: utf-8 -*-


import numpy as np
from matplotlib import pylab as plt

a = 1     
fs = 128
f0 = 25  
sec = 1   
value=[]

#サイン波を生成
for n in np.arange(fs * sec):
    s = a * np.sin(2.0 * np.pi * f0 * n / fs)
    value.append(s)

t = np.arange(0, len(value))/fs

np.savetxt('sin.csv', [t,value] ,fmt='%.5f',delimiter=',')

plt.plot(t,value)
plt.title('Fig.sine curve')
plt.xlabel('time')
plt.ylabel('sin()')
plt.xlim([0,1])
plt.show()