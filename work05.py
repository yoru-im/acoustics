# -*- coding: utf-8 -*-

import re

rs_freq = input('A4の周波数を入力してください：')

name = input('音名を入力してください：')


x = re.sub(r"\D","",name)
y = int(x) - 1
i = 3 + 12*y

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
    
    
if "#" in name:
    j += 1
    
elif "b" in name:
    j -= 1

    
keynum = i + j 
   
r = 2**(1/12)

freq = int(rs_freq)*r**(keynum-49)
print(freq,'Hz')
