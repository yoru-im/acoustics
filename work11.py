# -*- coding: utf-8 -*-

import wave
import numpy as np
import matplotlib.pyplot as plt

wfile = "A4.wav"
wf = wave.open(wfile, "rb")
ch = wf.getnchannels()
width = wf.getsampwidth()
fr = wf.getframerate()
fn = wf.getnframes()
time = 1.0 * fn/fr

#オーディオフレームの読み込みと1次元配列への変更
wdata = wf.readframes(wf.getnframes())
w = np.frombuffer(wdata, dtype = 'int16')

# 左チャンネル 0 番目から２ずつスライス
Lch = w[::2]

#t1,t2の入力
t1 = input('ｔ１秒の値を入力してください:')
t2 = input('t2秒の値を入力してください:')

#tの計算
t = np.arange(0, len(Lch))/fr

#グラフ化
plt.xlabel('time(sec)')
plt.ylabel('amplitude')
plt.plot(t,Lch)
plt.xlim(float(t1),float(t2))

plt.grid()
plt.show()

print()
print(f'ファイル名: {wfile}')
print(f'チャンネル数: {ch} ch')
print(f'サンプル幅: {width} byte')
print(f'サンプリング周波数: {fr} Hz')
print('長さ(秒):','{:.3f}'.format(time),'sec')
print()
print(f't1(sec): {t1}')
print(f't2(sec): {t2}')