"""

[우선순위 큐와 힙]

ref : https://suyeon96.tistory.com/31, https://www.daleseo.com/python-heapq/

1. 우선순위 큐(Priority Queue) : 일반적인 큐처럼 FIFO 구조가 아닌 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조
- Heap 자료구조를 이용하여 구현함

2. 힙(Heap) : 우선순위 큐를 위해 고안된 완전이진트리 형태의 자료구조
- 여러 개의 값 중 최댓값 또는 최솟값을 찾아내는 연산이 빠름
- 힙의 특징
    - 완전이진트리 형태로 이루어져 있음
    - 부모노드와 서브트리 간 대소 관계가 성립됨 (반정렬 상태)
    - 이진탐색트리(BST)와 달리 중복된 값이 허용됨
- 힙의 종류
    - 최대 힙(Max Heap) : 부모 노드의 키 값이 자식 노드보다 크거나 같은 완전이진트리(key_parent-node >= key_child-node)
    - 최소 힙(Min Heap) : 부모 노드의 키 값이 자식 노드보다 작거나 같은 완전이진트리(key_parent-node <= key_child-node)

"""

heap = []

# 힙에 원소 추가
from heapq import heappush

heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
