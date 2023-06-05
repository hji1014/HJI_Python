"""

[map() 함수]
: 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행하는 함수

(사용법)
map(function, iterable)

* iterable 자료형 : iter() 함수로 반복자를 리턴할 수 있는 타입,
str, list, tuple, dictionary, set, range가 있음

ref : https://blockdmask.tistory.com/531

"""
# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)

print(f'result1 : {result1}')


# map 함수 이용
def add_one(n):
    return n + 1


result2 = list(map(add_one, myList))  # map반환을 list 로 변환
print(f'result2 : {result2}')

# ================================================================= #

# map 과 lambda

# 일반 함수 이용
def func_mul(x):
    return x * 2


result1 = list(map(func_mul, [5, 4, 3, 2, 1]))
print(f"map(일반함수, 리스트) : {result1}")

# 람다 함수 이용
result2 = list(map(lambda x: x * 2, [5, 4, 3, 2, 1]))
print(f"map(람다함수, 리스트) : {result2}")

# ================================================================== #
n, m = map(int, input().split(' '))     # 띄어쓰기를 기준으로 n, m이라는 정수를 str로 입력 받을 때 사용

data = []
for i in range(m):
    data.append(list(map(int, input().split(' '))))      # 여러 개 데이터 입력 예시 (1) - 띄어쓰기로 구분

data = []
for i in range(m):
    data.append(list(map(int, input())))                 # 여러 개 데이터 입력 예시 (2) - 띄어쓰기 안할 때