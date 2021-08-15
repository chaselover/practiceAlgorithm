import sys
input = sys.stdin.readline


def isPossible(length):
    cnt = 0
    for pa in pas:
        cnt += pa//length
    if cnt >= C:
        return True
    return False


S, C = map(int, input().split())
pas = [int(input()) for _ in range(S)]

start = 1
end = max(pas)
answer = (start+end)//2
while start <= end:
    mid = (start+end)//2
    if isPossible(mid):
        start = mid+1
        answer = mid
    else:
        end = mid-1
rest = sum(pas) - answer*C

print(rest)