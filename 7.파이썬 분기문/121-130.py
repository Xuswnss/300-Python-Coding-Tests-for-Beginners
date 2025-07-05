import requests
# #121
# print('#121 is Lower?()')
# user = input()
# if user.islower():
#     print(user.upper())
# else: print(user.lower())
# print('- '* 10)

# #122
# print('#122 grade')
# user = input('학점을 입력하세요 : ')
# score = int(user)
# if score > 80:
#     print('A')
# elif score > 60:
#     print('B')
# elif score > 40:
#     print('C')
# elif score > 20:
#     print('D')
# else : print('E')
# print('- '* 10)

# #123
# print('#123 money..')

# # 환율 = {"달러": 1167, 
# #         "엔": 1.096, 
# #         "유로": 1268, 
# #         "위안": 171}
# # user = input("입력: ")

# # num, currency = user.split()
# # print(float(num) * 환율[currency], "원")

# print('- '* 10)

# #124
# print('#124 big number')
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)
    
    
# #125 
# print('#125 kt/skt/u+')
# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")


# #126
# print('#126 address')
# user = input('우편번호를 입력하세요 : ')
# num = user[:3]
# if num in ['010', '011', '012']:
#     print('강북구')
# elif num in ['013', '014', '015']:
#     print('도봉구')
# elif num in ['016', '017', '018', '019']:
#     print('노원구')

# #127
# print('#127')
# user = input('주민등록번호를 입력하세요 : ')
# user = user.split('-')[1]
# if user[0] == "1" or user[0] == "3":
#     print("남자")
# else:
#     print("여자")
    
# #128
# print('#128')
# user = input('주민등록번호를 입력해주세요 : ')
# user = user.split('-')[1]
# if 0 <= int(user[1:3]) <= 8:
#     print('seoul')
# else:
#     print('not seoul')

#129
print('#129')
#주민등록번호 첫번째부터 마지막 숫자 2- 부터 차례로 곱한다음 더한다.
#연산값을 11로 나누면 마지막 번호

# sum = 0
# user = input('주민번호를 입력해주세요 : ')
# print(user)
# modified_num = user.replace('-','').strip()

# weights = [2,3,4,5,6,7,8,9,2,3,4,5]
# for i in range(12):
#     sum = int(modified_num[i] * weights[i])
    
# print('x : ' ,sum)

# check_digit = (11 - (sum % 11)) % 10
# print("주민등록번호의 마지막 숫자:", modified_num[-1])
# print("계산된 검증번호:", check_digit)
# if int(modified_num[-1]) == check_digit:
#     print("유효한 주민등록번호입니다.")
# else:
    # print("유효하지 않은 주민등록번호입니다.")   
    
#130
print('#130 비트코인 바인딩')
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")


