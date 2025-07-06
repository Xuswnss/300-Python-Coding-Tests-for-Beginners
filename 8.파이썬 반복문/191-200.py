#191
print('#191')
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for line in data:
    for col in line:
        print('수수료 붙은 가격:',col * 1.00014)
        
print('- '*10)

#192
print('#192')

for line in data:
    for col in line:
        print('수수료 붙은 가격:',col * 1.00014)
    print('- '*10)
print('- '*10)

#193
print('#193')
result = []
for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)

        
print('- '*10)

#194
print('#194')
result = []
for line in data:
    sub = []
    for col in line:
        sub.append(float(col) * 1.00014)
    result.append(sub)
print(result)
print('- '*10)

#195
print('#195')
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    print(row[3])

print('- '*10)

#196
print('#196')
for row in ohlc[1:]:
    if row[3] > 150:
     print(row[3])


print('- '*10)

#197
print('#197')
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[3])
print('- '*10)

#198
print('#198')
#고가와 저가의 변동폭
for row in ohlc[1:]:
    # print(row)
    volatility = row[1] - row[2]
    print(volatility)
print('- '*10)

#199
print('#199')
for row in ohlc[1:]:
    volatility = row[1] - row[2]
    if row[3] >= row[0]:
        print(volatility)
print('- '*10)

#200
print('#200')
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])

print('- '*10)