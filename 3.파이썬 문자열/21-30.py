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
