"""

[알고리즘 코딩테스트를 위한 3가지 방법]

1. input() 함수 사용
2. sys 모듈 사용
3. txt 파일 읽어오기

"""

# ===================================================================================================== #

"""

[예제 입력 / ref : https://www.acmicpc.net/problem/2667]
- .txt 주소 : C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2667.txt

7
0110100
0110101
1110101
0000111            -> 띄어쓰기를 하지 않고 입력하는 경우
0100000
0111110
0111000

"""

# input() 함수 사용 -> 직접 입력
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# sys 모듈 사용 -> 직접 입력
import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# .txt 파일 읽어오기 -> 자동 입력
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_2667.txt', 'r')
n = int(f.readline().rstrip())
graph = []
for i in range(n):
    graph.append(list(map(int, f.readline().rstrip())))
f.close()

# ===================================================================================================== #

"""

[예제 입력 / ref : https://www.acmicpc.net/problem/1946]
- .txt 주소 : C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1946.txt

2
5
3 2
1 4
4 1
2 3
5 5
7                  -> 띄어쓰기 하고 입력하는 경우                   
3 6
7 3
4 2
1 4
5 7
2 5
6 1

"""
# input() 함수 사용 -> 직접 입력
t = int(input())
for _ in range(t):
    n = int(input())
    score = []
    for _ in range(n):
        score.append(list(map(int, input().split(' '))))

# sys 모듈 사용 -> 직접 입력
import sys
t = int(sys.stdin.readline().rstrip())
score = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        score.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

# .txt 파일 읽어오기 -> 자동 입력
f = open('C:/Users/User/Desktop/허준일/개인자료/취업준비/코딩테스트/test_case/BJ_1946.txt')
t = int(f.readline().rstrip())
for _ in range(t):
    n = int(f.readline().rstrip())
    score = []
    for _ in range(n):
        score.append(list(map(int, f.readline().rstrip().split(' '))))
f.close()