"""

[정렬(sorting) 관련 함수] - 1차원
1. sort()
2. sorted()

"""

# 1차원 배열 Ascending Sort, 오름차순(1, 2, 3, ...) 정렬
arr = [5, 2, 3, 1, 4]

a_sorted = sorted(arr)      # 변형X, 정렬된 새로운 배열 반환
print(a_sorted)

arr.sort()                  # 변형O, 반환 값 없음
print(arr)

# 1차원 배열 Descending Sort, 내림차순(5, 4, 3, ...) 정렬
arr = [5, 2, 3, 1, 4]

a_sorted = sorted(arr, reverse=True)      # 변형X, 정렬된 새로운 배열 반환
print(a_sorted)

arr.sort(reverse=True)                  # 변형O, 반환 값 없음
print(arr)

### 문자열 정렬은 sorted() 함수만 사용할 수 있음
# 문자열 정렬 - 하나의 덩어리일 때
str_arr = 'Zbcdefg'

a_sorted = sorted(str_arr)                  # 오름차순 : 대문자 -> 소문자 순
print(a_sorted)
a_sorted = sorted(str_arr, reverse=True)    # 내림차순 : 소문자 -> 대문자 순
print(a_sorted)

# 문자열 정렬 - 문장 입력일 때 단어를 sorting하는 방법
str_arr = "I'm like chardonnay, get better over time"

str_arr_split = sorted(str_arr.split())     # 단어 쪼개서 오름차순 정렬
print(str_arr_split)

str_arr_split = sorted(str_arr.split(), reverse=True)     # 단어 쪼개서 내림차순 정렬
print(str_arr_split)

str_arr_split = sorted(str_arr.split(), key=str.lower)     # 대소문자 구분하지 않고 정렬
print(str_arr_split)

# 2차원
# 리스트 정렬 시 key로 사용할 수 있는 lambda
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
b = sorted(a)           # key 안 넣고 sort() 또는 sorted() 사용 시 0열 기준으로 정렬
print(b)

c = sorted(a, key = lambda x : x[1])                # key 인자에 함수를 넘겨주면 우선순위가 정해짐
d = sorted(a, key=lambda x: x[1], reverse=True)     # 여기서는 1열 기준으로 정렬

e = sorted(a, key = lambda x : (x[0], -x[1]))       # 우선순위 : 0열 오름차순 -> 1열 내림차순
f = sorted(a, key = lambda x : -x[0])               # 0열 내림차순으로 정렬

# dictionary 자료형 sorting 방법
a = {'1' : 0.23, '2' : 0.5, '3' : 0.23}
a_sorted = sorted(a)                        # 이렇게 a를 통째로 넣으면 key를 기준으로 정렬하여 list가 생성됨
a_sorted = sorted(a, reverse=True)

b_sorted = sorted(a.items(), key=lambda x : x[1])                   # items() 함수를 쓰면 key와 value 중에 고른 것을 기준으로 sorting 함
b_sorted = sorted(a.items(), key=lambda x : x[1], reverse=True)     # reverse로 오름/내림차순 정할 수 있고, key는 같은 값일 때 오름차순으로 정렬됨
