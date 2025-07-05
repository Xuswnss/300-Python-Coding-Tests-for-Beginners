#141
print('#141')
리스트 = [100, 200, 300]
for i in 리스트:
    print( i + 10)

print('- '*10)

#142
print('#142')
list = ["김밥", "라면", "튀김"]
for menu in list:
    print('오늘의 메뉴 ; ', menu)

#143
print('#143')
list = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list:
    print(len(i))
print('- '*10)

#144
print('#144')
list = ['dog', 'cat', 'parrot']
for i in list:
    print(i , len(i))
print('- '*10) 
  
#145
print('#145')
list = ['dog', 'cat', 'parrot']
for i in list:
    print(i[0])
print('- '*10)

#146
print('#146')
list = [1, 2, 3 ]
for i in list :
    print( '3 x', i )
    
print('- '*10)


#147
print('#147')
list = [1, 2, 3]
for i in list :
    print( '3 x', i ,"=", 3 * i  ) 
print('- '*10)

#148
print("#148")
list = ["가", "나", "다", "라"]
나다라 = list[1:]
for i in 나다라:
    print(i)
print('- '*10)

#149
print('#149')
list = ["가", "나", "다", "라"]
newList = list[2:]
for i in newList:
    print(i)
print('- '*10)

#150
print('#150')
list = ["가", "나", "다", "라"]
for i in list[::-1]:
    print(i)
