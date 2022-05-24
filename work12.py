# -*- coding: utf-8 -*-

import numpy as np
import wave
import struct

fname = 'A3.wav'
ch = 1 
width = 2 #2byte = 16bit
fs = 44100 
f = 220 
time = 5 
samples = time * fs 

t = np.linspace(0, time, samples + 1) 
s = 30000 * np.sin(2 * np.pi * f * t)
s = np.rint(s) 
s = s.astype(np.int16) #符号あり16ビット整数型に変換
s = s[0:samples] 
data = struct.pack("h" * samples , *s) #bytesに変換

wf = wave.open(fname,'wb') 
wf.setnchannels(ch)                                                        
wf.setsampwidth(width)
wf.setframerate(fs) 
wf.writeframes(data)
wf.close() 

