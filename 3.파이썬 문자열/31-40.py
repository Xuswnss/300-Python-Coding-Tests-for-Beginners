#31
print('#31 문자열 합치기')
a = "3"
b = "4"
print(a + b)
print('- '*10)

#32
print('#32 문자열 곱하기')
print('h1' * 3)
print('- '*10)

#33
print('#33 문자열 곱하기')
print('- '*30)




#34
print('#34 문자열 곱하기')
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
print('- '*10)

#35
print('#35 print string')
name1 = 'jiyun'
age1 = 20
name2 = 'xuswns'
age2 = 1
print('name : %s age : %d' %(name1, age1))
print('name : %s, age: %d'%(name2,age2))

print('- '*10)
#36
print('#36 print string')
print('name : {}, age : {}'.format(name1, age2))
print('name : {}, age: {}'.format(name2, age2))
print('- '*10)

#37
print('#37 print string')
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
print('- '*10)

#38
print('#38 slice a string')
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
print('- '*10)

#39
print('#39 strip method')
data = "   삼성전자    "
#원본 유지 새로운 문자열 리턴
new_data  = data.strip()
print(new_data)
print('- '*10)

#40
print('#40 remove comma')
상장주식수 = "5,969,782,550"
numberOfOustandingShares = 상장주식수.replace(',','')
타입변환 = int(numberOfOustandingShares)
print(타입변환, type(타입변환))
