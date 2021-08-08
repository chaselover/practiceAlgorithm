import sys
input = sys.stdin.readline

def isPossible(target_time):
    balloon=0
    for staff in make_balloon:
        balloon += target_time//staff
    if balloon>=M:
        return True
    return False

N,M = map(int,input().split())
make_balloon = list(map(int,input().split()))

start = 0
end = 1e12
answer = 0
while start<=end:
    mid = (start+end)//2
    if isPossible(mid):
        end = mid-1
        answer=mid
    else:
        start = mid+1

print(int(answer))