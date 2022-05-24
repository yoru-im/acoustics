# -*- coding: utf-8 -*-

rs_freq = input('A4の周波数を入力してください：')
print(f'A4 = {rs_freq}Hz と入力されました')
print("（小数点以下3桁で表示）")

r = 2**(1/12)
for keynumber0 in range(88):
     keynumber = keynumber0 + 1
     freq = int(rs_freq)*r**(keynumber-49)
     print('【 No.',keynumber,'】','{:.3f}'.format(freq),'Hz')
     
     
