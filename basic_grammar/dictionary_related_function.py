"""

[사전형 관련 함수들]

1. 사전자료형 만드는 방법
2. 사전자료형의 key 또는 value만 다루기
3. 사전자료형의 key, value를 튜플형으로 반복문에 사용하기
4. items() 함수 사용하여 key와 value 쌍으로 얻기

"""

# 1. 사전자료형 만드는 방법
a = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}    # method(1)

num_dict = dict()           # method(2)
num_dict['zero'] = '0'
num_dict['one'] = '1'
num_dict['two'] = '2'
num_dict['three'] = '3'
num_dict['four'] = '4'
num_dict['five'] = '5'
num_dict['six'] = '6'
num_dict['seven'] = '7'
num_dict['eight'] = '8'
num_dict['nine'] = '9'

# 2. 사전자료형의 key 또는 value만 다루기
key_list = a.keys()
value_list = a.values()

# 3. 사전자료형의 key, value를 튜플형으로 반복문에 사용하기
for key, value in num_dict.items(): # 이 경우 key, value 각각 출력 가능
    print(key)
    print(value)

for i in num_dict.items():      # 이 경우 key, value 같이 출력 (tuple 형태로)
    print(i)

for i in num_dict:              # 이 경우 key만 출력
    print(i)

# 4. key와 value 쌍으로 얻기
a = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}    # method(1)
b = a.items()
c = list(a.items())
c[1][0]