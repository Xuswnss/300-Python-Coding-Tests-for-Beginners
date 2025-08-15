#231
print('#231')
def n_plus_1(n) :
    result = n + 1
    print(result)

n_plus_1(3)
print('- '*10)

#232
print('#232')
def make_url(string):
    result = f'www.{string}.com'
    print(result)

make_url('naver')

print('- '*10)

#233
print('#233')
def make_list(str):
    my_list =[]
    for i in str:
        my_list.append(i)
    return my_list
print('- '*10)

#234
print('#234')
def pickup_up(list):
    result = []
    for i in list:
       if i % 2 == 0:
           result.append(i)
    return result
print('- '*10)    

#235
print('#235')       
def convert_int(str):
    return int(str.replace(',',''))
print('- '*10)  

#236
print('#236')   
def fun(num):
    return num + 4
print('- '*10) 

#237
print('#237')
