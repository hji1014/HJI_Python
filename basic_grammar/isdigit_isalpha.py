"""

[문자열이 문자인지 숫자인지를 확인하여 True/False를 반환해주는 함수]
1. isdigit() : 문자열에 숫자만 있으면 True 반환
2. isalpha() : 문자열에 문자만 있으면 True 반환

"""

num = '123456'
num_str = '1aj321la2'
str = 'junil'

print(num.isdigit(), num.isalpha())
print('----------------------------')
print(num_str.isdigit(), num_str.isalpha())
print('----------------------------')
print(str.isdigit(), str.isalpha())
print('----------------------------')
