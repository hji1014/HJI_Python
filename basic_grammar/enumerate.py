"""

[인덱스와 원소를 동시에 접근할 수 있는 함수 - enumerate()]

ref: https://www.daleseo.com/python-enumerate/

"""

# 하나의 변수로
for entry in enumerate(['A', 'B', 'C']):
    print(entry)
    print(entry[0])
    print(entry[1])

# 두 개의 변수로
for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter)

# 시작 인덱스 변경
for i, letter in enumerate(['A', 'B', 'C'], start=1):
    print(i, letter)
