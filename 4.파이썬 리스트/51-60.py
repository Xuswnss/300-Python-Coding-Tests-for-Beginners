#51
print('#51 list creation')
movie_rank = ['닥터스트레인지', '스플릿', '럭키']
print(movie_rank)
print('- '*10)

#52
print('#52 append list')
movie_rank.append('베트맨')
print(movie_rank)
print('- '*10)

#53
print('#53 insert list ')
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
print('- '*10)

#54
print('#54 delete list')
del movie_rank[3]
print(movie_rank)
print('- '*10)

#55
print('#55 delete list')
del movie_rank[3]
del movie_rank[2] ## 여러 원소를 같이 삭제 할 수 없음!
print(movie_rank)
print('- '*10)

#56
print('#56 concatenate list')
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang = lang1 + lang2
print(lang)
print('- '*10)

#57
print('#57 min, max')
nums = [1, 2, 3, 4, 5, 6, 7]
print('min:', min(nums))
print('max:' , max(nums))
print('- '*10)

#58
print('#58 sum lists')
print(sum(nums))
print('- '*10)

#59
print('#59 number of data')
print(len(nums))
print('- '*10)

#60
print('#60 average list')
print(sum(nums) / len(nums))

