import sys
input = sys.stdin.readline

def DFS(i,sum_t):
    if i==N-1:
        answer.append(sum_t)
        return
    for x in tool:
        if x=='+' and tools[0]:
            tools[0] -=1
            DFS(i+1,sum_t+arr[i+1])
            tools[0] +=1
        elif x=='-' and tools[1]:
            tools[1] -=1
            DFS(i+1,sum_t-arr[i+1])
            tools[1] +=1
        elif x=='*' and tools[2]:
            tools[2] -=1
            DFS(i+1,sum_t*arr[i+1])
            tools[2] +=1
        else:
            if tools[3]:
                tools[3] -=1
                if sum_t>=0:
                    DFS(i+1,sum_t//arr[i+1])
                else:
                    DFS(i+1,-((-sum_t)//arr[i+1]))
                tools[3] +=1

N = int(input())
arr = list(map(int,input().split()))
tools = list(map(int,input().split()))
tool = '+-*/'
answer = []

DFS(0,arr[0])
# tools에서 N-1개롤 뽑는 조합.
# 최댓값과 최솟값 계산
print(max(answer))
print(min(answer))