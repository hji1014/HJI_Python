"""

[permutation 또는 combination으로 튜플 만들기]
(사용법)
import itertools
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):      # permutation(a, 3) -> 4P3
    실행문
for i in itertools.combinations(a, 3):      # combinations(a, 3) -> 4C3
    실행문

"""

# permutation
import itertools
a = [1, 2, 3, 4]
for i in itertools.permutations(a, 3):      # permutation(a, 3) -> 4P3
    print(i)

# combination
import itertools
a = [1, 2, 3, 4]
for i in itertools.combinations(a, 3):      # combinations(a, 3) -> 4C3
    print(i)

"""
리스트로 구현
ref: https://cotak.tistory.com/70
"""