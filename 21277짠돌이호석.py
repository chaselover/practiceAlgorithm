import sys
input=sys.stdin.readline

N,M = map(int,input().split())
puzzle = [list(map(int,list(input().rstrip()))) for _ in range(N)]
N2,M2 = map(int,input().split())
puzzle2 = [list(map(int,list(input().rstrip()))) for _ in range(N2)]

# 0도
# 90도
# 180도
# 270도
# 퍼즐 1,2를 동시에 탐색. 퍼즐1 0 퍼즐2 1이면 통과.
