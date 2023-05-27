"""

[2진수 비트연산자]

AND : &
OR : |
XOR : ^
NOT : ~

"""

# 13 = 0b1101, 9 = 0b1001
print(bin(0b1101 & 0b1101))         # AND
print(13 & 9)                       # AND

print(bin(0b1101 | 0b1101))         # OR
print(13 | 9)                       # OR

print(bin(0b1101 ^ 0b1101))         # XOR
print(13 ^ 9)                       # XOR

print(bin(~0b1101))                 # NOT
print(~13)                          # NOT