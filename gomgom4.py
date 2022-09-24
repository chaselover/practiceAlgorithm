import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
s = set()
for num in A:
    for num2 in set(s):
        tmp = (num + num2) % 7
        s.add(tmp)
    s.add(num % 7)
    if 4 in s:
        print("YES")
        exit()
print("NO")