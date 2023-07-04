"""

[hash 자료구조]

ref : https://go-coding.tistory.com/30
example : https://mgyo.tistory.com/177 (프로그래머스 - 완주하지 못한 선수)

* 자료구조를 배우는 이유 : 원하는 값을 최대한 효율적으로 찾을 수 있게 하기 위해 여러가지 '저장 구조'를 배우는 것

1. Hash 개념(from wiki) :
    - 해시 함수 : 임의의 데이터로부터 짧은 '전자 지문'을 만들어내는 방법
    - 해시 값 : 데이터를 해시 함수로 가공한 결과
    - 해시 테이블 : 자료 구조의 일종으로, 고유 키 값과 그에 따른 자료 값을 짝지을 때 해시 함수를 이용한다.

-> Hash table은 Hash를 주소로 삼아 데이터를 저장하는 자료구조

"""
data_array = ['HCH', 'OSN', 'HEJ', 'HJI', 'HSI']

# hash() 함수 사용하여 hash value 생성 후 hash table 만들기
hash_table = {}
for i in data_array:
    hash_table[hash(i)] = i     # hash(i) : hash value
