import sys
input = sys.stdin.readline

S = tuple(input().rstrip())

S_copy = S
S_copy = list(S_copy)
reverse_S = []
for _ in range(len(S)):
    reverse_S.append(S_copy.pop())
S = list(S)

print(1 if S==reverse_S else 0)