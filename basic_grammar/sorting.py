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