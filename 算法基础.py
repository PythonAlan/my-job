#!/usr/bin/env python3
#antuor:Alan

data = [[col for col in range(4)] for rowl in range(4)]

for a in data:
    print(a)

for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        tmp=data[c_index][r_index]
        data[c_index][r_index] = row[c_index]
        data[r_index][c_index] = tmp

    print('----------------')
    for r in data:print(r)
