import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
#1000000이 아닌 1000001...
F = [0]*1000001
stack=[0]
NGF = [-1]*N

# F(Ai) 등장횟수
for number in A:
    F[number] += 1


# NGF 오등큰수
for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
    i+=1


for ans in NGF:
    print(ans, end=" ")
