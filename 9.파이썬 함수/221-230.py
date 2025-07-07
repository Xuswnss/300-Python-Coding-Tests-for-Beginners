#221
print('#221')
def print_reverse(str):
    print(str[::-1])
    
print_reverse('python')
print('- ' * 10)

#222
print('#222')
def print_score(score):
    # sum = 0 
    # for i in score:
    #     sum += i
    # result = sum / len(score)
    # return result
    print(sum(score) / len(score))
print('- ' * 10)   

#223
print('#223')
def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)
            
print_even ([1, 3, 2, 10, 12, 11, 15])
print('- ' * 10) 

#224
print('#224')
def print_keys(list):
    for keys in list.keys():
        print(keys)
        
print_keys ({"이름":"김말똥", "나이":30, "성별":0})
print('- ' * 10) 

#225
print('#225')
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_keys(my_dict, key):
    print(my_dict[key])

print('- ' * 10) 

#226  
print('#226')
def print_5xn(line):
    num = int(len(line) / 5)
    for x in range(num + 1):
        print(x)
        print(line[x * 5 : x * 5 + 5])
print_5xn("아이엠어보이유알어걸")
       
#227
print('#227')
def print_mxn(line, num):
    num = int(len(line) / num )
    for x in range(num + 1 ):
        print(line[x * num : x * num + num])
print('- ' * 10) 

#228
print('#228')
def calc_monthly_salary(salary):
    monthly_pay = int( salary / 12)
    return salary
print('- ' * 10) 

#229
print('#229')
def my_print(a, b):
    print('left :',a)
    print('right :', b)
    
my_print(a = 100, b = 200)



    
