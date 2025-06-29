#21 
print('#21 문자열 인덱싱') 
#문자열에서 한 글자씩 가져오는 것을 인덱싱이라고 표현한다.
letter = 'python'
print(letter[0],letter[2])
print('- '*10)

#22
print('strings slice')
license_plate = "24가 2210"
#slicing에서 시작인덱스를 생략하면 0 끝인덱스를 생략하면 문자열에 끝을 의미한다.
#if you omit the start index in slicing, it defaults to 0 
#if you omit the end index, it means the end of strings
print(license_plate[-4::])


#23
print('#23 문자열 슬라이싱')
str ='홀짝홀짝홀짝'
## 변수명[start : end : offset]
print(str[::2])
print('- '*10)

#24
print('#24 문자열 역순 출력 ')
string = "PYTHON"
print(string[::-1])
print('- '*10)

#25
print('#25. 문자열 치환')
num = '010-1111-2222'
new_num = num.replace('-',' ')
print(new_num)
print('- '*10)

#26
print('#26 문자열 치환 ; replace a string')
num = '010-1111-2222'
new_num = num.replace('-','')
print(new_num)
print('- '*10)

#27
print('#27 도메인 출력')
url = "http://sharebook.kr"
new_url = url.split('.') # -> 문자열 배열 출력
print(new_url[-1])
print('- '*10)

#28
print('#28 문자열은 immutable')
# lang = 'python'
# lang[0] = 'P'
# print(lang)
print('문자열은 assignment(할당)메서드를 지원하지 않기 때문에 수정할 수 없다')
print('- '*10)

#29
print('#29 replace method')
string = 'abcdefagdafsal'
new_str = string.replace('a',"A")
print(new_str)
print('- '*10)
#30
print('#30. replace method')
string = 'abcd'
string.replace('b',"b")
#replace는 새로운 객체를 리턴하므로 원본은 변하지 않음
new_str = string.replace('b', 'B')
print(string)
print(new_str)
print('- '*10)




