import sys
input = sys.stdin.readline


lst = list(input().rstrip())
cursor = len(lst)
M = int(input())


for i in range(M):
    order = list(input().split())
    if order[0] == "L" and cursor != 0:
        cursor -=1
        continue
    if order[0] == "D" and cursor != len(lst):
        cursor +=1
        continue
    if order[0] =="P":
        lst.insert(cursor,order[1])
        cursor+=1
        continue
    if order[0] == "B" and cursor != 0:
        del lst[cursor-1]
        cursor-=1
        continue

print(''.join(lst))