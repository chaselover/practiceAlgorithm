

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int,input().split())))




cnt=0
for i in range(N-1):
    for j in range(i+1,N):
        x1,y1 = maps[i]
        x2,y2 = maps[j]
        try:
            k = y1 - ((y2-y1)/(x2-x1))*x1
        except:
            if x1==0 and x2==0:
                cnt+=1
            continue
        else:
            if k==0:
                cnt+=1

print(cnt)