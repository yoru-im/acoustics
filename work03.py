# -*- coding: utf-8 -*-

r = 2**(1/12)

f_name = input('出力ファイル名を入力してください：',)

f = open(f'{f_name}.txt', 'w')

rs_freq = input('A4の周波数を入力してください：')
print(f'{rs_freq}Hzと入力されました',file = f)
print(f'{rs_freq}Hzと入力されました')

for keynumber0 in range(88):
    keynumber = keynumber0 + 1
    freq = int(rs_freq)*r**(keynumber-49)
    print('【 No.',keynumber,'】',freq,'Hz',file = f)
    print('【 No.',keynumber,'】',freq,'Hz')

f.close()
