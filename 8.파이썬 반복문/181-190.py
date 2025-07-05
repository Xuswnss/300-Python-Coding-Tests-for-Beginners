#181
print('#181')
apart = [ ["101호", "102호"], ["201호", "202호"], ["301호", "302호"] ]
print('- '*10)

#182
print('#182')
stock = [ ["시가", 100, 200, 300], ["종가", 80, 210, 330] ]
print('- '*10)

#183
print('#183')
stock = { "시가" : [100, 200, 300], "종가" : [ 80,210,330 ]}
print('- '*10)

#184
print('#184')
stock = { "10/10" : [80,110,70,90], "10/11" : [210, 230, 190, 200]}
print('- '*10)

#185
print('#185')
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row: 
        print(col, '호')
print('- '*10)

#186
print('#186')
for row in apart[::-1]:
    for col in row:
        print(col, '호')
print('- '*10)

#187
print('#187')
for row in apart[::-1]:
    for col in row[::-1]:
        print(col,'호')
print('- '*10)

#188
print('#188')
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col , '호')
        print('---------')
print('- '*10)

#189
print('#189')
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")

#190
print('#190')
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col ,'호')
print('- '*5)