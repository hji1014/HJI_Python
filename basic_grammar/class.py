"""

[class 총정리]

ref : https://ybworld.tistory.com/20, https://kingnamji.tistory.com/6

- 공부 순서
(1) [Python/파이썬] Class(클래스) 기초 정리 - 1 : 개념, 사용법 -> 완료
(2) [Python/파이썬] Class(클래스) 기초 정리 - 2 : has-a 관계, 상속 개념 -> 완료
(3) [Python/파이썬] Class(클래스) 기초 정리 - 3 : 다중상속, super().__init__(), 메서드 오버라이딩 -> 완료
(4) [Python/파이썬] Class(클래스) 기초 정리 - 4 : 추상 클래스, 클래스 변수 -> 미완료
(5) [Python/파이썬] Class(클래스) 메서드 self 설명 -> 미완료

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

- Class는 주로 '객체 지향 프로그래밍'을 위해 필요한 개념 -> C++ / Java / Python에서 쓰임
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
    def ary_append(self, item): # 첫 번째 인수는 self임을 확인!
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
class Weapon():
    pass

# '무기' 클래스 객체 '칼'을 생성해보기
sword = Weapon()
print(type(sword))


""" Class 내부 변수 설정하기 """
# 무기 클래스 정의
class Weapon():
    power = 10
    strength = 20

# '무기' 클래스 객체 sword을 생성해보기"
sword = Weapon()
# 생성된 sword 객체를 통해 내부 변수에 접근하기
print("공격력 : ", sword.power)
print("착용시 근력증가 :", sword.strength)


""" Method 정의하고 호출하기 """
# 무기 클래스 정의
class Weapon():
    power = 10
    strength = 20

    def attack1(self):
        print("공격력"+str(self.power)+"으로 찌르기")       # self를 통해 class 내부 변수에 접근할 수 있음
    def attack2(self):
        print("근력"+str(self.strength)+"으로 던지기")

# '무기' 클래스 객체 sword을 생성해보기"
sword = Weapon()

# 생성된 sword 객체를 통해 내부 변수에 접근하기
print("칼로 할 수 있는 것 1")
sword.attack1()
print("칼로 할 수 있는 것 2")
sword.attack2()


""" 초기화 메서드 def __init__(self, ...) 이해하기(1) """
# 무기 클래스 정의
class Weapon():
    #초기화 메서드
    def __init__(self, what, power, action):
        print("무기종류 : ", what)
        print("공격력 : ", power)
        print("기능 : ", action)

# sword 라는 객체 생성
sword = Weapon("Sword", "10", "찌른다")
# gun 이라는 객체 생성
gun = Weapon("Gun", "20", "쏜다")


""" 초기화 메서드 def __init__(self, ...) 이해하기(2) """
# 무기 클래스 정의
class Weapon():
    # 초기화 메서드, 인수2개 전달(어떤 무기인지, 공격력)
    def __init__(self, what, power):
        self.what_weapon = what
        self.power_num = power

    # 클래스 내부 메소드 구문 : 초기화 메서드에서 설정한 클래스 변수들 사용
    def action1(self):
        print(self.what_weapon + "은 공격력" + self.power_num + "으로 찌른다")

    def action2(self):
        print(self.what_weapon + "은 공격력" + self.power_num + "으로 쏜다")

# 무기 Class의 객체 sword 생성
sword = Weapon("Sword", "10")
sword.action1()

# 무기 Class의 객체 gun 생성
gun = Weapon("Gun", "20")
gun.action2()


""" 인스턴스, 인스턴스 변수 """
# 무기 클래스를 선언. 내부 내용은 아무 것도 없음(pass)
class Weapon:
    pass

# sword 객체 선언
sword = Weapon()
sword.power = 10
sword.level = 5

# gun 객체 선언
gun = Weapon()
gun.power = 20
gun.type = "원거리"

# 같은 class이지만 각각 다른 변수를 가질 수 있다.
print("칼의 공격력 : ", sword.power)
print("칼의 레벨제한 : ", sword.level)
print("총의 공격력 : ", gun.power)
print("총의 공격타입 : ", gun.type)


""" has - a 관계 """
# has - a 관계는 객체가 다른 객체를 포함한다는 뜻
# RPG 게임에는 소지품을 보관할 수 있는 인벤토리(혹은 가방, 창고) 개념이 있음
# 인벤토리도 생각해보면 또 다른 클래스 개념으로 생각할 수 있음
# 인벤토리는 보관 최대 개수, 공간 등의 속성을 가짐
# 무기 클래스의 창과 총(객체)는 이 게임 유저의 인벤토리(객체)에 들어갈 수 있음
# 이러한 관게를 has - a 관계라고 함
class Inventory:
    # 인벤토리 기본속성 : 닫혀있다. 빈공간이다.(리스트로 선언)
    def __init__(self):
        self.opened = False
        self.item_space = []

    # 인벤토리 열기 메소드 : 열려있는 상태로 변경한다.
    def open(self):
        self.opened = True
        print("인벤토리가 열렸습니다. 아이템을 넣을 수 있습니다.")

    # 인벤토리에 아이템 넣기 메소드 : 기본 속성인 item_space에 아이템을 추가한다.
    def put(self, something):
        if self.opened == True:
            self.item_space.append(something)
            print('아이템을 인벤토리에 넣었습니다.')
        else:
            print("인벤토리를 먼저 열어주세요")

    # 인벤토리 닫기 메소드 : 닫혀있는 상태로 변경한다.
    def close(self):
        self.opened = False
        print("인벤토리를 닫았습니다.")

class Weapon:
    pass

sword = Weapon()
item_bag = Inventory()

# 아이템 인벤토리를 연다.
item_bag.open()

# 칼을 인벤토리에 넣어보자.
item_bag.put(sword)

# item_space 에 접근하여 뭐가 있는지 확인해보자.
print("인벤토리에 보유중인 아이템 : ", item_bag.item_space)

# 인벤토리를 닫자
item_bag.close()


""" 상속(Inheritance) """
# 상속은 어떠한 클래스가 다른 클래스의 메서드(내부 함수), 속성(내부 변수)을 물려받을 수 있는 것을 의미함
# 부모, 자식 간의 관계라고 생각하여 물려주는 클래스는 '부모 클래스', 물려받는 클래스는 '자식 클래스(=하위 클래스)'라고 함
# Class 상속 사용법 -> Class 'Class명'('상속받을 Class명'):
# 상속을 하는 이유 : 1) 기존 클래스를 그대로 유지하기 위해, 2) 코드 관리의 편의성을 위해

# 무기 클래스 선언
class Weapon:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        print("저는 무기 클래스입니다! 공격할 수 있습니다!!")

    # 무기의 종류를 출력하는 메소드
    def what_weapon(self):
        print("어떤 타입이야? :", self.type)
        print("어떤 무기야? : ", self.name)

# Sword라는 클래스를 선언하고 Weapon 클래스를 상속한다.
class Sword(Weapon):
    pass

# Sword 클래스 객체 선언
short_sword = Sword("근거리", "단검")

# 부모 클래스의 메소드인 what_weapon() 호출
short_sword.what_weapon()


""" 다중 상속(Multiple Inheritance) """
# Weapon 클래스 정의
class Weapon:
    def attack(self):
        print("무기는 공격할 수 있어!")

# Thing 클래스 정의
class Thing:
    def sell(self):
        print("나는 물건이니 판매할 수도 있지")

# Sword 클래스 정의 : Weapon과 Thing 클래스 상속
class Sword(Weapon, Thing):
    pass

short_sword = Sword()               # Sword 클래스 객체 short_sword 선언
short_sword.attack()                # Weapon 클래스의 메소드 호출
short_sword.sell()                  # Thing 클래스의 메소드 호출


""" super().__init__() """
# 부모 클래스의 초기화 메서드(def __init__(self):) 호출하기
# 자식 클래스에서 초기화 메서드를 사용하지 않으면 해당 방법을 사용하지 않아도 됨
# 아래 오류 구문에서는 super().__init__()을 사용하지 않음

####################################### 오류 구문 #######################################

# Weapon 클래스 정의
class Weapon:
    def __init__(self):
        self.what = "무기"
        self.type = "근거리"
        print("나는 무기 클래스다!")

# Sword 클래스 정의 : Weapon 클래스 상속
class Sword(Weapon):
    def __init__(self, power, level):
        self.power = power
        self.level = level

    # Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
    def info(self):
       print("공격력 : ",self.power)
       print("필요레벨 : ",self.level)
       print("무기종류 : ", self.what)
       print("공격타입 : ", self.type)

# Sword 클래스 객체 short_sword 선언
short_sword = Sword(10, 20)
short_sword.info()

#####################################################################################


##################################### 정상 구문(1) #####################################
class Weapon:
    def __init__(self):
        self.what = "무기"
        self.type = "근거리"
        print("나는 무기 클래스다!")

# Sword 클래스 정의 : Weapon 클래스 상속
class Sword(Weapon):
    def __init__(self, power, level):
        super().__init__()
        self.power = power
        self.level = level

    # Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
    def info(self):
        print("공격력 : ", self.power)
        print("필요레벨 : ", self.level)
        print("무기종류 : ", self.what)
        print("공격타입 : ", self.type)

# Sword 클래스 객체 short_sword 선언
short_sword = Sword(10, 20)
short_sword.info()

#####################################################################################


##################################### 정상 구문(2) #####################################
class Weapon:
    def __init__(self, what, type):
        self.what = what
        self.type = type
        print("나는 무기 클래스다!")

# Sword 클래스 정의 : Weapon 클래스 상속
class Sword(Weapon):
    def __init__(self, power, level, what, type):
        super().__init__(what, type)
        self.power = power
        self.level = level

    # Sword 속성(power,level) 및 부모 클래스 Weapon 의 속성 불러오기(what, type)
    def info(self):
        print("공격력 : ", self.power)
        print("필요레벨 : ", self.level)
        print("무기종류 : ", self.what)
        print("공격타입 : ", self.type)

# Sword 클래스 객체 short_sword 선언
short_sword = Sword(10, 20, "단검", "근거리")
short_sword.info()

#####################################################################################


""" 메서드 오버라이딩 """
# 메서드 오버라이딩은 클래스 상속 관게에서 자식 클래스가 부모 클래스의 메서드를 덮어써서 다른 함수로 사용하는 것
# super().attack 안 하면, 자식 클래스의 메서드만 호출됨

# Weapon 클래스 정의
class Weapon:
   def attack(self):
       print("무기는 공격할 수 있다")

# Sword 클래스 정의 : Weapon 클래스 상속
class Sword(Weapon):
    def attack(self):                   # 메서드 오버라이딩
        print("칼을 무엇이든지 벨 수 있다")
        super().attack()                # 부모 클래스의 attack 메서드 호출

short_sword = Sword()
short_sword.attack()
