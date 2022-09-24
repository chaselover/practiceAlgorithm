import sys
input = sys.stdin.readline

def DFS(idx,calculate):
    if idx==N:
        answer.append(calculate)
        return
    num = seqs[idx]
    for operator in '+-*/':
        if operator == '+'and opers[0]:
            opers[0] -=1
            DFS(idx+1,calculate+num)
            opers[0] +=1
        elif operator == '-' and opers[1]:
            opers[1] -=1
            DFS(idx+1,calculate-num)
            opers[1] +=1
        elif operator == '*' and opers[2]:
            opers[2] -=1
            DFS(idx+1,calculate*num)
            opers[2] +=1
        elif operator == '/' and opers[3]:
            if calculate <0:
                opers[3] -=1
                DFS(idx+1,-((-calculate)//num))
                opers[3] +=1
            else:
                opers[3] -=1
                DFS(idx+1,calculate//num)
                opers[3] +=1

N = int(input())
seqs = list(map(int,input().split()))
opers = list(map(int,input().split()))
answer=[]

DFS(1,seqs[0])

print(max(answer))
print(min(answer))