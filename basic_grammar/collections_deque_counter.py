"""

[collections 모듈]

1. deque : que 또는 스택을 구현하는 함수
- 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없음
- 그러나, 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용됨
- 첫 번째 원소 삭제 : popleft()
- 마지막 원소 삭제 : pop()
- 첫 번째 원소 삽입 : appendleft(x)
- 마지막 원소 삭제 : append(x)

2. counter : 등장 횟수를 세는 기능을 제공
- 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려줌

"""

# deque
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))   # list 자료형으로 변환

# counter
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['red'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))