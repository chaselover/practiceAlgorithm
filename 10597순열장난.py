import sys
from collections import deque


def DFS(idx):
    # idx 1부터 시작 kriii의 검사가 모두 끝나면 수열의 가장 큰 값을 찾는다.
    if idx == len(kriii):
        high = 0
        for i in range(len(sequence)):
            high = max(high,int(sequence[i]))
        # 가장 큰 값이 수열의 길이와 같으면 출력, 아니면 회귀
        if high == len(sequence):
            print(*list(map(int,(sequence))))
            sys.exit()            
        return
    # dfs로 배열에 하나넣거나 두개는경우를 동시에 둘 다 조사하며 재귀 진행.(분기가 있는 DFS)
    # 글자 하나만 조사.idx 하나 건너뛴다.
    if idx < len(kriii) and int(kriii[idx]) <= 50 and not visited[int(kriii[idx])]:
        visited[int(kriii[idx])] = 1
        sequence.append(kriii[idx])
        DFS(idx+1)
        sequence.pop()
        visited[int(kriii[idx])] = 0

    # 글자 두개조사. 두개짤랐을때 50이하. 그리고 그 숫자가 전에 방문한적 없었을때 방문.idx 2개 건너뛴다.
    if idx + 1 < len(kriii) and int(kriii[idx:idx+2]) <= 50 and not visited[int(kriii[idx:idx+2])]:
        visited[int(kriii[idx:idx+2])] = 1
        sequence.append(kriii[idx:idx+2])
        DFS(idx+2)
        visited[int(kriii[idx:idx+2])] = 0
        sequence.pop()
    

kriii = input()
sequence = deque()
visited = [0] * 51
DFS(0)
