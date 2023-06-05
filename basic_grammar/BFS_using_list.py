"""

[Breadth First Search (BFS) 알고리즘을 list로 구현하는 방법]

- 삼성계열사 코딩테스트에서는 import를 사용할 수 없고 내장 함수만 사용할 수 있음
- 따라서 본 코드를 이해하여야 함
ref : https://data-marketing-bk.tistory.com/entry/BFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

"""

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def bfs(graph, start_node):
    need_visited, visited = [], []              # need_visited : 방문 해야할 곳, visited : 방문한 곳
    need_visited.append(start_node)             # 가장 처음 방문 해야할 곳에 start node 추가

    while need_visited:                         # need_visited 빌 때까지 반복
        node = need_visited[0]
        del need_visited[0]                     # 여기서 비어도 마지막까지 코드를 돌린 다음에 종료하는 것 (?)
        if node not in visited:                 # 현재 node가 visited에 없으면...
            visited.append(node)                # visited에 노드 추가
            need_visited.extend(graph[node])    # append는 리스트를 그대로 추가하고, extend는 리스트(if iterable)의 각 항목들을 차례로 넣음
    return visited

a = bfs(graph, 'A')
