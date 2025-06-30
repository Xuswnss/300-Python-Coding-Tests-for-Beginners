#61
print('#61 slicing method()')
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
print('- ' * 10)

#62
print('#62 slicing method()')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print('- ' * 10)

#63
print('#63 slicing method()')
print(nums[1::2])
print('- ' * 10)

#63
print('#64 slicing method()')
print(nums[::-1])
print('- ' * 10)

#65
print('#65 바인딩')
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
print('- ' * 10)

#66 
print('#66 join method()')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest))
print('- ' * 10)

#67
print('#67 join method()')
print('/'.join(interest))
print('- ' * 10)

#68
print('#68 join method()')
print('\n'.join(interest))
print('- ' * 10)

#69
print('#69 split() method')
string = "삼성전자/LG전자/Naver"
print(string.split('/'))
print('- ' * 10)

#70
print('#70 오름차순')
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))