#151
print('#151')
list = [3, -20, -3, 44]
for i in list:
    if i < 0:
        print( i )
        
print('- '*10)

#152
print('#152')
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)
print('- '*10)
       
#153
print('#153')
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i < 20 :
        if i % 3 == 0:
            print(i)
print('- '*10)     
      
#154
print('#154')
list = ["I", "study", "python", "language", "!"]
for i in list[1:4]:
    print(i)
    
print('- '*10)      

#155
print('#155')
list = ["A", "b", "c", "D"]
for i in list:
    if i.isupper():
        print(i)
print('- '*10) 

#157
print('#157')
for i in list:
    if i.isupper() == False:
        print(i)
print('- '*10) 
        
#158
print('#158')
list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
    i= i.split(".")
    print(i[0])
print('- '*10) 

#159
print('#159')    
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    new = i.split('.')[1]
    if new[0] == 'h':
        print(i)


#160
print('#160')
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
    new = i.split('.')[1]
    if new[0] == 'h' or new[0] == 'c':
        print(i)

