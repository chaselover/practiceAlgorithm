import sys 
sys.setrecursionlimit(10**6) 

n = int(input()) 
in_order = list(map(int, input().split())) 
post_order = list(map(int, input().split())) 

pos = [0]*(n+1) 
for i in range(n): 
    pos[in_order[i]] = i # 중위 순회로 부모노드의 위치에서 왼쪽에 몇개있나 알수있음


def divide(in_start, in_end, p_start, p_end): # 중위 시작, 끝, 후위시작, 끝 / 트리 나누면서 계속 나누어감.(트리 나눌때마다 인덱스 조정을 위한 것.)
    if(in_start > in_end) or (p_start > p_end): 
        return 
    parents = post_order[p_end] # 후위순회에서 부모노드 찾기 (후위순회의 마지막 노드가 루트) / 후위순회의 뒤에있을수록 level이 낮은 node(부모노드)
    print(parents, end=" ") 
    
    left = pos[parents] - in_start # 왼쪽인자 갯수 (루트노드기준 왼쪽)
    right = in_end - pos[parents] # 오른쪽인자 갯수 (루트노드기준 오른쪽)

    divide(in_start, in_start+left-1, p_start, p_start+left-1) # 왼쪽 트리(왼쪽 부분트리로 들어가 거기서 부모노드 찾고 왼쪽 오른쪽 나눈다.) 중위 시작 똑같고 끝은 왼쪽갯수-1인덱스고 후위시작 똑같고 후위끝 왼쪽 갯수-1
    divide(in_end-right+1, in_end, p_end-right, p_end-1) # 오른쪽 트리 (오른쪽 부모노드 찾고 왼쪽 오른쪽 나눈다.) 중위 시작 중위끝에서 오른쪽갯수만큼 뺀것. 중위 끝 똑같고 후위 시작은 후위 끝에서 오른쪽 갯수만큼 빼고 후위끝은 그냥 -1인덱스.

divide(0, n-1, 0, n-1)



