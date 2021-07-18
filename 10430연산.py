A, B= map(int,input().split())
C, D=A,B

while A%B != 0:
    if A>B:
        A = A%B
    if B>A:
        B = B%A

print(A)

print((C/A)*D)