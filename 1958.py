import sys

S = sys.stdin.readline()
P = sys.stdin.readline()

if P in S:
    print(1)
else:
    print(S,P)