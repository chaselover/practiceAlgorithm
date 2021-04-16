import sys

A = list(sys.stdin.readline())
B = list(sys.stdin.readline())
A.pop()
B.pop()
cnt = 0
dp = [[0]*len(B) for _ in range(len(A))]


for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:


print(dp)

ACAYKP
CAPCAK