"""

[shallow & deep copy 함수]

shallow -> 복사한 객체가 원본 객체의 주소를 바라보고 있음 -> 원본 값을 변경하면 복사 값도 변경되는 문제 발생

"""

# shallow copy (1) '=' 대입 연산자
arr1 = [1, 2, 3]
arr2 = arr1
arr1.append(4)

# shallow copy (2) [:] 슬라이싱
arr1 = [1, 2, 3, [4, 5, 6], 7]
arr2 = arr1[:]
arr1[3].append(1000)

# shallow copy (3) copy() 함수
arr1 = [1, 2, 3, [4, 5, 6], 7]
arr2 = arr1.copy()
arr1[3].append(1000)

# deep copy
import copy
arr1 = [1, 2, 3, [4, 5, 6], 7]
arr2 = copy.deepcopy(arr1)
arr1[3].append(1000)
