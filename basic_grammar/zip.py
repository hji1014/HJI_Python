"""

[zip() 함수]
- 여러 개의 순회가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환함

"""

# 튜플로 반환
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
for pair in zip(numbers, letters):
    print(pair)

# 병렬 처리
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
for num, letter in zip(numbers, letters):
    print(f'num은 {num}이고 알파벳은 {letter}입니다.')
