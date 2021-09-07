import sys
input = sys.stdin.readline
from bisect import bisect_left
sys.setrecursionlimit(10**6)


def checking(next_circle, my_right):
    # 다음원의 오른쪽과 내 오른쪽이 겹치면?
    if circles[next_circle][1] == my_right:
        return 1
    # 안겹치면 ? 나랑 그 다음 겹치는 놈을 찾으러 들어감.
    elif circles[next_circle][1] != my_right:
        tmp =bisect_left(circles,[circles[next_circle][1],]) 
        if circles[tmp][0] is not None and circles[tmp][0] == circles[next_circle][1]:
            return 1* checking(tmp,my_right)
        else:
            return 0
    else:
        return 0


n = int(input())
circles= []
for _ in range(n):
    center , radius=  map(int,input().split())
    circles.append([center-radius , center + radius])
circles.sort( key= lambda x:( x[0], -x[1]))

ans = 2
for i in range(n-1):
    if circles[i][0] == circles[i+1][0]:
        # 완전히 겹칠때
        if circles[i][1] == circles[i+1][1]:
            ans+=1
        # 안쪽으로 겹칠때
        else:
            next_circle = bisect_left(circles,[circles[i+1][1],])
            # 오른쪽도 접하는 원이 있다면?
            try:
                if circles[next_circle][0] == circles[i+1][1]:
                    # 나랑 그 다음원까지 원
                    if checking(next_circle, circles[i][1]):
                        ans +=2
                    # 나만 원
                    else:
                        ans +=1
                # 왼쪽만 접하는 원.
                else:
                    ans+=1
            except:
                ans += 1
    # 왼쪽 겹침.
    else:
        ans +=1
print(ans)
        

# 다른풀이/.
import sys
from bisect import bisect_left
input = sys.stdin.readline
sys.setrecursionlimit(400000)

def next_circle(cur_c,next_c):
    global cnt
    if circles[cur_c][1] == circles[next_c][1]:
        cnt += 1
        return
    tmp = bisect_left(circles,(circles[next_c][1],))
    if tmp == len(circles):
        return
    if circles[tmp][0]==circles[next_c][1]:
        next_circle(cur_c,tmp)


n = int(input())
circles = []
for i in range(n):
	x,r = map(int,input().split())
	circles.append((x-r,x+r))
circles.sort(key=lambda x:(x[0],-x[1]))

cnt = 0
for i in range(n-1):
	if circles[i][0] == circles[i+1][0]:
		next_circle(i,i+1)
print(n+cnt+1)