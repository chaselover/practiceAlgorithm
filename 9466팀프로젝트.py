import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_cycle(cur_node):
    global cnt
    check_cycle[cur_node] = True
    cycle_stack.append(cur_node)
    next_node = choices[cur_node]
    if not check_cycle[next_node]:
        find_cycle(next_node)
    else:
        if next_node in cycle_stack:
            cnt -= len(cycle_stack[cycle_stack.index(next_node):])
# 프로젝트 팀원 수 제한 없음 팀 하나만 만들어질수도 있음,
# 모든 학생은 1명씩 함께 하고픈 팀원 선택. 자기자신 선택 가능(혼자하고프면)
# 선택지가 사이클을 이루면 한팀. -> 사이클을 이루지 못하는 학생의 수.

for test in range(int(input())):
    n = int(input())
    choices = [0] + list(map(int,input().split()))
    check_cycle = {i:False for i in range(1,n+1)}
    
    cnt=n
    for i in range(1,n+1):
        if not check_cycle[i]:
            cycle_stack=[]
            find_cycle(i)

    print(cnt)