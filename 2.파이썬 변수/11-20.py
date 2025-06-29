#11
print('#11 삼성전자라는 변수로 50,000원을 바인딩 해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요')
samsung = 50000
price = samsung * 10
print('총 평가금액',price)
print('- '* 10)
#12
print('#12 삼성전자의 일부 투자 정보입니다. 변수를 사용해서 시가총액, 현재가, per등을 바인딩 해보세요')
marketCapitalization = 298000000000
currentPrice = 50000
per = 15.79
print('시가총액', marketCapitalization)
print('현재가', currentPrice)
print('PER', per)
print('- '* 10)

#13
print('#13 문자열 출력')
s = 'hello'
t = 'python'
print(s+ "!" ,t)
print('- '* 10)
#14
print('#14 파이썬을 이용한 값 계산')
print(2+2*3)
print('- '* 10)

#15
print('#15 type 함수')
a= 2
print(type(a))
print('- '* 10)

#16
print('#16 string to Int')
num_str = "720"
num_int = int(num_str) # string to integer
print(num_int+1, type(num_int))

print('- '* 10)

#17
print('#17 integer to string')
num = 100
num_str = str(num)
print(num_str, type(num_str))
print('- '* 10)

#18
print('#18 String to float')
data = "15.79"
data = float(data)
print(data, type(data))
print('- '* 10)

#19
print('#19 문자열 정수 변환')
year = "2024"
year_int = int(2024)
print(year_int -1)
print(year_int -2)
print(year_int -3)

print('- '* 10)

#20
print('#20 무이자 36개월치 계산')
month = 48584 
result = month * 36
print(result)
print('- '* 10)
