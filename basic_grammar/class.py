"""

[class 총정리]

ref : https://ybworld.tistory.com/20, https://kingnamji.tistory.com/6

- Class를 쉽게 게임의 '아이템'의 개념으로 생각하면 됨
- 예를 들어, RPG 게임에는 공격, 방어할 수 있는 여러 아이템이 존재 -> 무기, 갑옷, 장신구, 신발(각각 class로 생각)
- 그 중, 무기를 상세적으로 분류해보면 칼, 총, 지팡이, 도끼 등이 있고 이 속에서 아이템의 스킬, 특수효과 등의 속성이 있음
    - 무기는 '공격', 갑옷은 '방어' 등을 말함 -> 속성 or 메서드
    - 무기에는 도끼, 칼, 총 등 여러 분류가 있고 각 무기들을 무기의 공통적인 특성을 가지고 있음 -> 상속

    무기 clss():
        * 속성 1 : 공격력
        * 속성 2 : 레벨제한
        * 속성 3 : Type

            Sword():
                공격력 : 10
                레벨제한 : Level 5 이상
                Type : 근거리

                기능 [1] : 벤다
                기능 [2] : 찌른다

            Gun():
                공격력 : 20
                레벨제한 : Level 15 이상
                Type : 원거리

                기능 [1] : 쏜다
                기능 [2] : 때린다

- Class는 주로 '객체 지향 프로그래밍'을 위해 필요한 개념 -> C++ / Python에서 쓰임
- 또한 Class를 어떤 '틀'로 생각하면 됨. -> 똑같은 무엇을 계속 만들어 내는 것으로 비유
- Class는 객체(object)를 정의하고 만들기 위한 변수와 메서드의 집합
- 와플틀 : class / 만들어진 와플 : 객체(object) -> 객체들은 서로 영향을 끼치지 않음

<예시 코드>
class car():
    def on(self):
        print("차량의 시동을 켭니다.")

ray = car()
ray.on()

<출력 결과>
차량의 시동을 켭니다.

- 위의 예시 코드에서 ray는 객체(object)이고, ray 객체는 car 클래스의 인스턴스(instance), on은 메서드(method)임
- 즉 instance는 클래스의 객체가 소프트웨어에 실체화된 것을 의미함
- 메서드 속성은 클래스 안에서 구현하는 함수를 의미

<예시 코드>
class example(): # example라는 이름의 클래스를 만듭니다.
    def __init__(self):
        self.ary = []
        print('__init__()메서드를 통해 객체를 초기화 했습니다.')

    # 메서드를 하나 정의합니다.
    def ary_append(self, item): # 첫 번째 인수는 self 임을 확인!
        self.ary.append(item)

ex1 = example()
print(ex1.ary)

ex1.ary_append(10)
print(ex1.ary)

<출력 결과>
__init__()메서드를 통해 객체를 초기화 했습니다.
[]
[10]

- 메서드의 첫 번째 매개변수 이름은 클래스의 인스턴스 자신임 -> 따라서 관례적으로 self라는 이름으로 사용
- 메서드 이름이 __init__인 경우 이 메서드를 생성자(constructor)라고 함
- 생성자는 객체가 생성되면 자동으로 호출돼 객체를 초기화함

<예시 코드>
class Hello(): # Hello라는 이름의 클래스를 만듭니다.
    def __init__(self,value): # 객체를 초기화하는 메서드
        self.value = value
        print('__init__()메서드를 통해 객체를 초기화 했습니다.')
        print(f'인스턴스의 value 값은 {self.value}입니다.')

ex2 = Hello(20)

<출력 결과>
__init__()메서드를 통해 객체를 초기화 했습니다.
인스턴스의 value 값은 20입니다.

"""


""" Class 정의 """
# 무기 클래스 정의
class Weapone():
    pass

# '무기' 클래스 객체 '칼'을 생성해보기
sword = Weapone()
print(type(sword))


""" Class 내부 변수 설정하기 """
# 무기 클래스 정의
class Weapone():
    power = 10
    strength = 20

# '무기' 클래스 객체 sword을 생성해보기"
sword = Weapone()
# 생성된 sword 객체를 통해 내부 변수에 접근하기
print("공격력 : ", sword.power)
print("착용시 근력증가 :", sword.strength)


""" Method 정의하고 호출하기 """
# 무기 클래스 정의
class Weapone():
    power = 10
    strength = 20

    def attack1(self):
        print("공격력"+str(self.power)+"으로 찌르기")       # self를 통해 class 내부 변수에 접근할 수 있음
    def attack2(self):
        print("근력"+str(self.strength)+"으로 던지기")

# '무기' 클래스 객체 sword을 생성해보기"
sword = Weapone()

# 생성된 sword 객체를 통해 내부 변수에 접근하기
print("칼로 할 수 있는 것 1")
sword.attack1()
print("칼로 할 수 있는 것 2")
sword.attack2()


""" 초기화 메서드 def __init__(self, ...) 이해하기(1) """
# 무기 클래스 정의
class Weapone():
    #초기화 메서드
    def __init__(self, what, power, action):
        print("무기종류 : ", what)
        print("공격력 : ", power)
        print("기능 : ", action)

# sword 라는 객체 생성
sword = Weapone("Sword", "10", "찌른다")
# gun 이라는 객체 생성
gun = Weapone("Gun", "20", "쏜다")


""" 초기화 메서드 def __init__(self, ...) 이해하기(2) """


# 무기 클래스 정의
class Weapone():
    # 초기화 메서드, 인수2개 전달(어떤 무기인지, 공격력)
    def __init__(self, what, power):
        self.what_weapone = what
        self.power_num = power

    # 클래스 내부 메소드 구문 : 초기화 메서드에서 설정한 클래스 변수들 사용
    def action1(self):
        print(self.what_weapone + "은 공격력" + self.power_num + "으로 찌른다")

    def action2(self):
        print(self.what_weapone + "은 공격력" + self.power_num + "으로 쏜다")


# 무기 Class의 객체 sword 생성
sword = Weapone("Sword", "10")
sword.action1()

# 무기 Class의 객체 gun 생성
gun = Weapone("Gun", "20")
gun.action2()

