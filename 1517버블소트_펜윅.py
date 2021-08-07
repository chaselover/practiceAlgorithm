import sys

# fenwick_update : 펜윅 트리인 tree의 idx번째 노드를 d로 갱신하는 함수
def fenwick_update(tree, idx, d):
    while idx <= n:
        tree[idx] += d
        idx += (idx & -idx)

# fenwick_find : 펜윅 트리인 tree의 start번째 노드부터 end번째 노드까지의 합을 리턴하는 함수
def fenwick_find(tree, start, end):
    if end < start:
        return 0
    res = 0
    idx = end
    while idx > 0:
        res += tree[idx]
        idx -= (idx & -idx)
    idx = start - 1
    while idx > 0:
        res -= tree[idx]
        idx -= (idx & -idx)
    return res

# relation_convert : 배열 arr의 원소들을 대소 관계를 유지하는 상대 값으로 바꾼 배열을 리턴하는 함수
def relation_convert(arr):
    sort_arr = sorted(arr)
    mid = dict().fromkeys(sort_arr, 0)
    res = []
    visited = [False] * (len(arr) + 1)
    for idx, temp in enumerate(mid):
        mid[temp] = idx + 1
    for i in arr:
        if visited[mid[i]] == False:
            res.append(mid[i])
            visited[mid[i]] = True
    return res
    
# 입력부
n = int(sys.stdin.readline())
before = list(map(int, sys.stdin.readline().split()))

# after = before의 상대 배열
after = relation_convert(before)

# ftr : 펜윅 트리
ftr = [0] * (n + 1)
ans = 0
for i in range(len(after)):
    # 자신보다 큰 수의 갯수를 ans에 저장하고
    ans += (fenwick_find(ftr, after[i], len(after)))
    # 저장했으면 자신을 넣는다
    fenwick_update(ftr, after[i], 1)
    
# 정답 출력
print(ans)