"""

[람다(lambda)]
: 의미 익명함수를 지칭하는 용어 즉, 기존의 함수(명 등)을 선언하고
사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수.
1. 람다(lambda)
2. 리스트 정렬 시 key로 사용할 수 있는 lambda
3. map() 표현식
4. filter() 표현식

ref : https://gorokke.tistory.com/38

"""
# 람다(lambda)
# 형식 -> lambda 인자 : 표현식
# 예시 -> sum = lambda x:x+1
(lambda x : x + 10)(1)                                      # 인자 한 개 사용
(lambda x, y : x + y)(1, 10)                                 # 인자 두 개 사용
check_pass = lambda x : 'pass' if x >= 70 else 'fail'     # 조건문 사용
check_pass(100)

# 리스트 정렬 시 key로 사용할 수 있는 lambda
a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]
b = sorted(a)           # key 안 넣고 sort() 또는 sorted() 사용 시 0열 기준으로 정렬
print(b)

c = sorted(a, key = lambda x : x[1])                # key 인자에 함수를 넘겨주면 우선순위가 정해짐
d = sorted(a, key=lambda x: x[1], reverse=True)     # 여기서는 1열 기준으로 정렬

e = sorted(a, key = lambda x : (x[0], -x[1]))       # 우선순위 : 0열 오름차순 -> 1열 내림차순
f = sorted(a, key = lambda x : -x[0])               # 0열 내림차순으로 정렬

s = ['2 A', '1 B', '4 C', '1 A']
ss = sorted(s, key=lambda x: (x.split(' ')[1], x.split(' ')[0]))

# map 표현식
print(list(map(lambda x : x + 10, [1, 2, 3])))

# filter() 표현식
a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]
result = list(filter(lambda x : x > 7 and x < 15, a))