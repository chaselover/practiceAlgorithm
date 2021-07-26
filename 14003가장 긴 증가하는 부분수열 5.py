import sys
from bisect import bisect_left
input = sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

# 현 배열과 이진탐색 리스트. 
q=[]
temp=[]
for x in a:
    # 큐가 비어있거나 증가수열인자일때 넣는다. temp에는 q에 x가 들어간 위치를 표시한다. //그냥 마지막 인자보다 크면 깔금하게 넣고
    if not q or x>q[-1]:
        q.append(x)
        temp.append((len(q)-1,x))
    else:
        # 이진탐색으로 queue내에서 x의 index를 찾은 후 그 값을 x로 변경. 마지막 인자보다 작으면 안에서 나보다 큰놈 찾아서 앞으로 들어간다.
        q[bisect_left(q,x)]=x
        # temp에도 동일하게 x의 위치와 인자를 삽입해준다.
        temp.append((bisect_left(q,x),x))

ans=[]
last_idx=len(q)-1
# 검사한 모든 인자 idx부터 0번 인덱스까지 역순으로 검사한다.
for i in range(len(temp)-1,-1,-1):
    # temp의 index값이 큐에 들어간 마지막 인덱스 값과 같다면
    if temp[i][0]==last_idx:
        # 엔서에 그 tmp인자x를 삽입하고 검사 인덱스를 한단계 낮춘다.
        ans.append(temp[i][1])
        last_idx-=1
        # 총 길이와
print(len(ans))
# ans배열을 뒤집어 순서대로 출력한다.
print(*reversed(ans))


"""
bisect_left 구현.

def lower_bound(start,end,x):
    while start < end:
        mid = (start+end)//2

        if tmp[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end
"""