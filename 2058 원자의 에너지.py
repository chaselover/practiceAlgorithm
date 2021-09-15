import sys
input = sys.stdin.readline

# tree에 진입합니다.
def dfs(cur_atom):
    visited[cur_atom] = True
    dp[cur_atom][1] = cur_atom
    for gap in plus:                    # plus는 양성자크기들의 배열입니다.
        next_atom = cur_atom + gap      # 다음 노드는 지금 노드에서 양성자를 더해 갈수있는 위치입니다.
        if next_atom in visited:
            dfs(next_atom)
                                        # 상태인자 1은 현 노드를 가져가는 선택지, 0은 가져가지 않는 선택지입니다.
            dp[cur_atom][0] += max(dp[next_atom][1], dp[next_atom][0])      
            dp[cur_atom][1] += dp[next_atom][0]

# 각 atom_e상태가 plus를 받아들이거나 빼서 다른 atom_e에 도달할 수 있다.
# 그러나 인접한 에너지 준위가 존재하면 안된다.
# 어떤 atom_e의 조합을 선택해야 합이 최대가 되는가?
N, M = map(int, input().split())
atom_e = [int(input()) for _ in range(N)]
atom_e.sort()                                   # 낮은 에너지 준위부터 검사하기 위한 정렬
visited = {atom: False for atom in atom_e}      # 한번 방문한 노드를 방문하지 않기위한 check_list
dp = {atom: [0,0] for atom in atom_e}           # 각 선택지에 대해 최댓값을 저장할 dict
plus = [int(input()) for _ in range(M)]         # 각 에너지 준위 간의 차이값이 될 선택지인 양성자 크기 배열

max_sum = 0
for atom in atom_e:
    if not visited[atom]:                       # 모든 에너지준위에 대해 검사
        dfs(atom)
        max_sum += max(dp[atom][0], dp[atom][1])
print(max_sum)