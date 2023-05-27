"""

[오른쪽/왼쪽 정렬 + 특정 값으로 빈 곳 채우기]

rjust() : 오른쪽 정렬 + 특정 문자로 왼쪽 공백 채우기
ljust() : 왼쪽 정렬 + 특정 문자로 오른쪽 공백 채우기

"""

# rjust(맞출 문자 수, '공백에 넣을 문자')
val = "77".rjust(5, "0")
print(val)

val = "77777".rjust(5, "0")
print(val)

val = "123".rjust(5, "a")
print(val)

val = "123".rjust(3, "a")
print(val)

# ljust(맞출 문자 수, '공백에 넣을 문자')
val = "222".ljust(3, "0")
print(val)

val = "222".ljust(15, "a")
print(val)