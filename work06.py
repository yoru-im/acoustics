# -*- coding: utf-8 -*-


name = input('コードネームを入力してください：')

cord = ['C','(Db)C#','D','(Eb)D#','E','F','(Gb)F#','G','(Ab)G#','A','(Bb)A#','B']

if name[0] == 'C':
    r = 0
   
elif name[0] == 'D':
    r = 2
    
elif name[0] == 'E':
    r = 4
    
elif name[0] == 'F':
    r = 5
    
elif name[0] == 'G':
    r = 7
    
elif name[0] == 'A':
    r = 9
    
elif name[0] == 'B':
    r = 11  
    
    
if "#" in name:
    r += 1
    
elif "b" in name:
    r -= 1
    
    
M3rd = r + 4
m3rd = r + 3
c5th = r + 7

if M3rd >= 12:
    M3rd -= 12
if m3rd >= 12:
    m3rd -= 12
if c5th >= 12:
    c5th -= 12


if "m" in name:
    print(f'コードの構成音は 【{cord[r]},{cord[m3rd]},{cord[c5th]}】 です')
else:
    print(f'コードの構成音は 【{cord[r]},{cord[M3rd]},{cord[c5th]}】 です')