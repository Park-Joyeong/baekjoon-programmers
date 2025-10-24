# 첫째 줄에 , 둘째 줄에 , 셋째 줄에 , 넷째 줄에 를 출력한다.

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)