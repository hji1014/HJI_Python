"""

[join() 함수]
: 리스트를 문자열로 일정하게 합쳐주는 함수

(사용법)
''.join(리스트)
'구분자'.join(리스트)

ref : https://blockdmask.tistory.com/468 , https://resilient-923.tistory.com/264

"""
# 구분자 없이 바로 합치거나, 구분자를 기준으로 합쳐 문자열을 출력하는 방법
a = ['a', 'b', 'c', 'd', '1', '2', '100']
b = ''.join(a)
c = '+'.join(a)
d = '_____'.join(a)

# 문자열에 list 씌우면 글자, 기호, 띄어쓰기 하나하나 별로 나눠서 리스트에 저장됨
e = '내 이름은 허준일입니다.'
f = list(e)