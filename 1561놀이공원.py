import sys
input = sys.stdin.readline

def isPossible(mid):
    cnt=0
    for i in range(M):
        cnt += mid//amusement[i] + 1
    if cnt >=N:
        return True
    return False
# N명의 아이들 한줄
# M개의 1인승 놀이기구
# 운행시간 지나면 탑승하고 있던 아이 내리고 줄 맨앞에 있던 아이가 빈 놀이기구로 들어감.
# 동시에 비어있으면 제일 앞에있는 놀이기구.

N,M=map(int,input().split())
amusement = list(map(int,input().split()))

start=0
end = 6e10
answer=0
while start <= end:
    mid = (start + end)//2
    if isPossible(mid):
        end = mid-1
        answer=mid
    else:
        start = mid+1

cnt_last_time =0
for i in range(M):
    cnt_last_time += (answer-1)//amusement[i] + 1

for i in range(M):
    if not answer%amusement[i]:
        cnt_last_time+=1
        if cnt_last_time==N:
            print(i+1)
            exit()