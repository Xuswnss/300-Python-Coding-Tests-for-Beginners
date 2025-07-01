#111
print('#111 문자열 두번 출력')
user = input('입력 : ')
print(user * 2)
print('- ' *10)

#112
print('#112 user input()')
user = input('숫자를 입력하세요')
print( user + 10)
print('- ' *10)

#113
print('#113 user input()')
user = input('숫자를 입력하세요')
if int(user)% 2 == 0:
    print('even')
else: print('odd')
print('- ' *10)

#114
print('#114 user input()')
user = input('숫자를 입력하세요')
if user >= 255 :
    print(225)
else: 
    print( int(user) + 20)
    
print('- ' *10)

#115
print('#115 user input()')
user = input('숫자를 입력하세요')
num = int(user) - 20
if num <= 0:
    print(0)
elif num > 255:
    print(255)
else: print(num)
    
print('- ' *10)


#116
print('#116 user input()')
user= input('시간을 입력해주세요 : ')
if user[-2 :] == "00":
    print('정각입니다')
else: print('정각이 아닙니다.')
print('- ' *10)

#117
print('#117 user input()')  
fruit = ["사과", "포도", "홍시"]
  
user = input('좋아하는 과일은? : ')
if user in fruit:
    print('정답입니다')
else: print('오류입니다.')
print('- ' *10)

#118
print('#118 user input()') 
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input('종목명 : ')
if user in warn_investment_list:
    print('투자 경고 종목입니다')
else : print('투자 경고 종목이 아닙니다.')
print('- ' *10)

#119 - #120
print('#119 user input()') 
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if user in fruit:
    print('정답입니다')
else: print('오답입니다')

if user in fruit.values():
    print('정답입니다')
else: print('오답입니다.')
print('- ' *10)