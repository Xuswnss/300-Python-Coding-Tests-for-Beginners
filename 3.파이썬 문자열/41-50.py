#41
print('#41 upper method')
ticker = "btc_krw"
print(ticker.upper())
print('- '*10)

#42
print('#42 upper method')
ticker = "btc_krw"
print(ticker.lower())
print('- '*10)

#43
print('#43 capitalize method')
str = 'hello'
str = str.capitalize()
print(str)
print('- '*10)

#44
print('#44. endswith method')
file_name = "보고서.xlsx"
isTrue  = file_name.endswith('xlsx')
print('is file endswith xlsx? : ' , isTrue)
print('- '*10)

#45
print('#45. endswith method')
isTrue  = file_name.endswith(('xlsx', 'xls')) # or
print('is file endswith xlsx? : ' , isTrue)
print('- '*10)

#46
print('#46 startswit mehtod')
file_name = "2020_보고서.xlsx"
isTrue = file_name.startswith('2020')
print('is file startswith 2020? : ' , isTrue)
print('- '*10)

#46
print('#46 split method')
a = "hello world"
a.split()
print(a.split())
print('- '*10)

#47
print('#47 split method')
data = "btc_krw"
print(data.split('_'))
print('- '*10)

#48
print('#48 split method')
date = "2020-05-01"
print(date.split("-"))
print('- '*10)

#49
print('#49 rstrip method')
data = "039490     "
print(data.rstrip())