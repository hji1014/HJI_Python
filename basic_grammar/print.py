"""

[print() 출력 함수]

1. 기본적인 print() 함수
2. 여려 번 print() 사용하여 한 줄에 표현하기

"""

# 기본적인 print() 함수
a = [1, 2, 3, 4, 5, 'a']
print(a)                    # print(a, end='\n') -> default
print(a[3])                 # 즉 기본적으로 print() 사용할 때마다 줄 바꿔쓰기 포함
print(a[5])

# 여러 번 print() 사용하여 한 줄에 표현하기

print(1, end=' ')          # print(a, end=' ') -> end 인자를 ' '로 변경
print(2)                    # 한 줄에 1 2를 같이 출력할 수 있음