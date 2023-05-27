"""

[문자열의 특정 값을 원하는 문자로 변경하는 함수]

replace(old, new, [count])
- old : 현재 문자열에서 변경하고 싶은 문자
- new: 새로 바꿀 문자
- count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다.

"""

a = 'hello world'
b = a.replace('hello', "what's up?")
print(a)
print(b)

c = '1011101011'
d = c.replace('1', '#')