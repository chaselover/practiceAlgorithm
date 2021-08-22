import sys
input = sys.stdin.readline
from collections import defaultdict

while 1:
    n = int(input())
    if not n:
        break
    strings = []
    lower_dict = defaultdict(str)
    for _ in range(n):
        s = input().rstrip()
        l = s.lower()
        lower_dict[l] = s
        strings.append(l)
    strings.sort()
    print(lower_dict[strings[0]])
    
    