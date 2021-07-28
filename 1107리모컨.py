import sys
input = sys.stdin.readline

def can_push_num(num):
    num = list(str(num))
    for i in num:
        if i in broken: 
            return False
    return True

target = int(input())
m = int(input())
broken = list(input().split())
min_push = abs(target - 100)
for i in range(1000001):
    if can_push_num(i): 
        min_push = min(min_push, len(str(i)) + abs(i - target))
print(min_push)