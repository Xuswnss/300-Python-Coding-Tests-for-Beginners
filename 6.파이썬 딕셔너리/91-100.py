#91
print('#91 make dic')
inventory = { 
    '메로나' : [300,20],
    '비비빅' : [400, 3],
    '죠스바' : [250, 100]
    
             }
print(inventory)
print('- '*10)

#92
print('#92 indexing dictionary')
print(inventory['메로나'][0],"won")
print('- '*10)

#93
print('#93 indexing dictionary')
print(inventory['메로나'][1], '개')
print('- '*10)

#94
print('#94 add inventory item')
inventory['월드콘'] = [500, 7]
print(inventory)
print('- '*10)

#95
print('#95 dictionary key method()')
print(list(inventory.keys()))
print('- '*10)

#96
print('#96 dictionary values() method')
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))
print('- '*10)

#97
print('#97 dictionary values() method')
print(list(icecream.values()))
print('- '*10)

#98
print('#98 dictionary update method')
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
print('추가하기 전 : ',icecream)

icecream.update(new_product)
print('new:',icecream)
print('- '*10)

#99
print('#99 zip and dict')
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
#dict() -> new empty dictionary dict(mapping) 
# -> new dictionary initialized from a mapping object's
#(key, value) pairs
result = dict(zip(keys, vals)) # keys, vals로 구성된 새로운 딕셔너리를 만든다
print(result)
print('- '*10)

#100
print('#100 zip and dict')
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_price = dict(zip(date, close_price))
print(close_price)
