# -*- coding: utf-8 -*-


import numpy as np

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

