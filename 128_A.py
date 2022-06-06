import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    candi = set()
    for num in range(l1, r1 + 1):
        candi.add(num)
    for num in range(l2, r2 + 1):
        if num in candi:
            print(num)
            break
    else:
        print(l1 + l2)
