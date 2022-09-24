import sys

A = list(sys.stdin.readline())
B = list(sys.stdin.readline())
A.pop()
B.pop()
cnt = 0
dp = []


for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            for m in range(min(len(A)-i,len(B)-j)):
                if A[i+m]==B[j+m]:
                    cnt+=1
                else:
                    dp.append(cnt)
                    cnt=0
                    break

print(dp)

