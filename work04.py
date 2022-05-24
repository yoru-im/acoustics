# -*- coding: utf-8 -*-


rs_freq = input('A4の周波数を入力してください：')
print(f'A4 = {rs_freq}Hz　とします')
name = input('音名を入力してください：')


k = int(name[1]) - 1
i = 3 + 12*k

if name[0] == 'C':
    j = 1
   
elif name[0] == 'D':
    j = 3
    
elif name[0] == 'E':
    j = 5
    
elif name[0] == 'F':
    j = 6
    
elif name[0] == 'G':
    j = 8
    
elif name[0] == 'A':
    j = 10
    
elif name[0] == 'B':
    j = 12   
    
keynum = i + j 
     
r = 2**(1/12)

freq = int(rs_freq)*r**(keynum-49)
print('{:.3f}'.format(freq),'Hz','(小数点以下3桁で表示)')
