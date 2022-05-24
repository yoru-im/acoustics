# -*- coding: utf-8 -*-


import wave
import numpy as np
 
wf = wave.open("A3.wav" , "rb" )


buf = wf.readframes(wf.getnframes())
data = np.frombuffer(buf, dtype="int16")#16bitに変換

#16bitは音の最大値と最小値の値を2^16に分割する（-32768~+32768）
data = data / 32678 #振幅

rate = wf.getframerate()
time = np.arange(0,data.shape[0]/rate,1/rate)

np.savetxt('work13.csv', [time,data] ,fmt='%.5f',delimiter=',')
