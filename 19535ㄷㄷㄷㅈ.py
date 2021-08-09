import sys
read = sys.stdin.readline

# 조합을 팩토리얼로 구함(a~(a-b+1))까지 곱한값 분자 1~b까지 곱한값 분모.
def set_combination_cnt(a, b):
    com_cnt = 1
    if a-b < b:
        b = a-b
    for i in range(a-b+1, a+1):
        com_cnt *= i
    for j in range(1, b+1):
        com_cnt //=j
    return com_cnt

N = int(read())
edge = []
edge_cnt = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, read().split())
    edge.append([a, b])
    edge_cnt[a] += 1
    edge_cnt[b] += 1

du_tree_cnt = 0
ga_tree_cnt = 0
# 각 간선양쪽에서 이어진 선분 수만큼 ㄷ Tree가 있음(가운데선분 고정 양쪽 선분 선택.)
for start,end in edge:
    temp = (edge_cnt[start]-1) * (edge_cnt[end]-1)
    du_tree_cnt += temp
# ㅈ 트리는 간선이 3개 이상일때 그 중에서 3개를 뽑느 조합의 수만큼 나옴.
for idx in range(1, N+1):
    if edge_cnt[idx] >= 3:
        ga_tree_cnt += set_combination_cnt(edge_cnt[idx], 3)

#print(du_tree_cnt, ga_tree_cnt)

if du_tree_cnt > 3 * ga_tree_cnt:
    print('D')
elif du_tree_cnt < 3 * ga_tree_cnt:
    print('G')
else:
    print('DUDUDUNGA')