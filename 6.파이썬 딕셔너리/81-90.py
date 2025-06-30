#별 표현식
# 기본적으로 데이터 언패킹은 좌변과 우변의 데이터 개수가 같아야 한다. 하지만 star expression을 사용하면 
# 변수의 개수가 다랄도 데이터를 언패킹할 수 있다. 

#81
print('#81 data unpacking star expression ')
a, b, *c = (0, 1, 2, 3, 4, 5)
print(f'a : {a}, b : {b}, c:{c}')
print('- '*10)


#82
print('#82 data unpacking star expression')
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b , *valid_score = scores
print(valid_score)
print('- '*10)

#83
print('#84 data unpacking star expression')
a, *valid_score, b = scores
print(valid_score)
print('- '*10)

#84
print('#84 make dic')
temp = {}
print(temp , type(temp))
print('- '*10)

#85
print('#85  make dic')
temp = {
    "메로나" : 1000,
    "폴라포" : 1200,
    "빵빠레" : 1000 
}
print(temp)
print('- '*10)

#86
print('#86 add dic item')
temp['죠스바'] =1200
temp['월드콘'] = 1500
print(temp)
print('- '*10)

#87
print('#87 how much 메로나')
print('메로나 가격:',temp['메로나'])
print('- '*10)

#88
print('#88 modify 메로나')
temp['메로나'] = 1300
print(temp['메로나'])
print('- '*10)

#89
print('#89 delete merona')
del temp['메로나']
print(temp)
print('- '*10)