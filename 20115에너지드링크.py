import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))

x.sort()
total = x[-1]
for i in range(N-1):
    total += x[i]/2
print(total)