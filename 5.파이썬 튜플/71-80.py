#71
print('#71 creation tuple')
my_variable = ()
print(type(my_variable))
print('- '*10)

#72
print('#72 creation movie_rank tuple')
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)
print('- '*10)

#73
print('#73 create a tuple that sores the numeber 1')
a = (1)
print(a)
print('- '*10)

#74
print('#74 튜플은 원소(Element)값을 변경할 수 없습니다')
print('- '*10)

#75
print('#75 binding')
t = 1, 2, 3, 4
print('튜플은 중괄호가 없어도 동작 합니다:',type(t))
print('- '*10)

#76
print('#76 modify tuple')
t = ('a', 'b', 'c')
print('tuple does not change')
print('- '*10)

#77
print('#77 tuple to list')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest, type(interest))
print('- '*10)

#78
print('#78 list to tuple')
interest = tuple(interest)
print(interest, type(interest))
print('- '*10)

#79
print('#79 tuple unpacking')
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print('- '*10)

#80
print('#80 tuple range')
data = tuple(range(2,100,2))
print(f'짝수 출력 {data}')