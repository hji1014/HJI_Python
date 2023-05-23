"""

[continue, pass, break 각각의 설명과 차이점]

1. continue : 하위 모든 코드를 건너뛰고 다음 순번의 loop를 수행함
2. pass : 실행할 코드가 없는 것으로 다음 행동을 수행함
3. break : 반복문을 멈추고 loop 밖으로 나감

"""

# continue
# i가 짝수가 되는 경우 continue가 실행되고, 하위 코드인 print(i)를 수행하지 않고 다음 loop로 넘어감
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# pass
# pass는 그냥 진짜 '아무것도' 하지 않고 다음 줄(단계)로 넘어갈 때 사용
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        pass
    print(i)

# break
# break문이 실행되는 순간 for, while 등의 반복문에서 loop 밖으로 탈출
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        break
    print(i)