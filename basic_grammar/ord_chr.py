"""

[ord(), chr() 함수]

(사용법)
1) ord
ord('문자1개') : 문자의 아스키코드를 알려줌 (정수로)
chr(정수) : 아스키코드 정수를 입력하면 문자로 변환해줌

"""

a = 'a'
print(ord(a))

b = 97
print(chr(b))

# 참고 응용코드
# 시저 암호 (프로그래머스)
def solution(s, n):
    answer = ''
    #print(ord('A'), ord('Z'), ord('a'), ord('z'))
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i].isupper():
            num = (ord(s[i]) - 65 + n) % 26     # 0과 25 사이로 만들어 놓고 shifting을 시켜준 이후에 26으로 나눈 나머지 값은 어짜피 0~25 사이로 나옴. 이게 핵심
            answer += chr(num + 65)
        elif s[i].islower():
            num = (ord(s[i]) - 97 + n) % 26
            answer += chr(num + 97)
        else:
            pass
    return answer