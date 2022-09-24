import sys
input = sys.stdin.readline

def Binary(start,end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        old = houses[0]
        cnt=1

        for i in range(1,len(houses)):
            if houses[i] >= old+mid:
                cnt+=1
                old = houses[i]
        if cnt >=C:
            start = mid+1
            result=mid
        else:
            end = mid-1
    return result

N,C = map(int,input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
    
houses.sort()

start = 1
end = houses[-1]-houses[0]


print(Binary(start,end))