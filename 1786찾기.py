import sys
input = sys.stdin.readline


def MakeTable(P,KMPTable):
    j = 0
    for i in range(1,len(P)):
        while j > 0 and P[i]!=P[j]: # 같지 않을 때
            j = KMPTable[j-1] # 이전의 맞은부분까지 돌아가서 다시 비교
        if P[i]==P[j]: # 같을 시
            j += 1 # j증가시키고
            KMPTable[i] = j # table 갱신

def KMP(T,P,KMPTable):
    MakeTable(P,KMPTable)
    j = 0
    count = 0
    result = []
    P_size = len(P)
    for i in range(len(T)):
        while j > 0 and T[i]!=P[j]: # 같지 않을 때
            j = KMPTable[j-1] # 이전의 맞은 부분까지 돌아가서 다시 비교
        if T[i]==P[j]: # 같으면
            if j ==P_size-1:
                count += 1 # 갯수 추가
                result.append(i-P_size+2) # 위치 추가
                j = KMPTable[j] # 위치 옮겨주고 다시 탐색
            else: # j늘려준다.
                j += 1
    return count, result

T = input().rstrip()
P = input().rstrip()

KMPTable = [0 for _ in range(len(P))]

cnt, answer = KMP(T,P,KMPTable)
print(cnt)
print(*answer)