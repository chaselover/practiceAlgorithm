import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

def is_rotate(cur_gire,next_gire):
    if next_gire==cur_gire+1:
        if check_rotate[cur_gire][2]!=check_rotate[next_gire][6]:
            return True
    elif next_gire==cur_gire-1:
        if check_rotate[next_gire][2]!=check_rotate[cur_gire][6]:
            return True
    return False

def do_rotate(cur_gire,cur_dir):
    queue=[]
    queue.append([cur_gire,cur_dir])
    finished=[False]*4
    gires[cur_gire].rotate(cur_dir)
    finished[cur_gire] = True
    while queue:
        cur_gire,cur_dir = queue.pop()
        for next_gire in (cur_gire+1,cur_gire-1):
            if 0<=next_gire<4 and not finished[next_gire]:
                if is_rotate(cur_gire,next_gire):
                    queue.append([next_gire,-cur_dir])
                    gires[next_gire].rotate(-cur_dir)
                    finished[next_gire] = True

gires = []
for _ in range(4):
    q=deque()
    temp = list(map(int,list(input().rstrip())))
    for num in temp:
        q.append(num)
    gires.append(q)
K = int(input())

for _ in range(K):
    gire_num,dir = map(int,input().split())
    check_rotate=deepcopy(gires)
    do_rotate(gire_num-1,dir)

score=[1,2,4,8]
total=0
for i in range(4):
    total+=gires[i][0]*score[i]

print(total)