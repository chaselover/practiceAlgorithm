import sys
from collections import deque


def DFS(idx):
    if idx == len(kriii):
        high = 0
        for i in range(len(sequence)):
            high = max(high,int(sequence[i]))
        
        if high == len(sequence):
            print(*list(map(int,(sequence))))
            sys.exit()            
        return

    if idx < len(kriii) and int(kriii[idx]) <= 50 and not visited[int(kriii[idx])]:
        visited[int(kriii[idx])] = 1
        sequence.append(kriii[idx])
        DFS(idx+1)
        sequence.pop()
        visited[int(kriii[idx])] = 0

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
