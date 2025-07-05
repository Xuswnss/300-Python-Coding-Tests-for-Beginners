#171
print('#171')
price_list = [32100, 32150, 32000, 32500]
for i in price_list:
    print(i)
print('- '*10)

#172
print('#172')
num = 0
for i in price_list:
    print(num, i)
    num = num + 1
print('- '*10)

#173
print('#173')
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print( (3 - i ) ,price_list[i])
print('- '*10)

#174
print('#174')
num = 100
for i in range(len(price_list)):
    print( num, price_list[0] )
    num += 10
print('- '*10)

#175
print('#175')
my_list = ["가", "나", "다", "라"]
for i in range(1 , len(my_list)):
    print(my_list[i-1], my_list[i])
print('- '*10)

#176
print('#176')
for i in range(2, len(my_list)):
    print(my_list[i-2], my_list[i-1], my_list[i])
print('- '*10)

#177
print('#177')
my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])
print('- '*10)

#179
print('#178')
my_list = [100, 200, 400, 800]
#abs -> 절댓값 변화
for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))


#180
print('#180')
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])