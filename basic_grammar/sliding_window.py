"""

[sliding window 구현]
: 원형 테이블에 1번부터 10번까지 차례로 앉아있다고 했을 때,
1번부터 3명씩 이어 붙여 출력하고 싶다.
하지만 일반적인 인덱싱 방법을 사용하면 [9, 10, 1], [10, 1, 2]의 배열을 출력할 수 없다.

위와 같은 문제를 해결하기 위해 sliding window를 사용할 수 있다.

"""

# window_size=3 인 sliding window 구현
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lp, rp = 0, 0
window_size = 3
while lp != 10:
    rp = lp + window_size
    p = []
    for i in range(lp, rp):
        i = i % len(a)
        p.append(a[i])
    print(p)
    lp += 1
