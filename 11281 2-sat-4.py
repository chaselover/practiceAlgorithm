# 타잔
import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(2 * N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[-a].append(b)
    graph[-b].append(a)

scc_num = 1
idx = 1
stack = []
scc_idx = [0] * (2 * N + 1)
check = [0] * (2 * N + 1)
visit = [0] * (2 * N + 1)

def SCC(node):
    global idx, scc_num
    visit[node] = idx
    root = idx
    idx += 1
    stack.append(node)

    for nxt in graph[node]:
        if not visit[nxt]:
            root = min(root, SCC(nxt))
        elif not check[nxt]:
            root = min(root, visit[nxt])

    if root == visit[node]:
        while stack:
            top = stack.pop()
            check[top] = 1
            scc_idx[top] = scc_num
            if node == top:
                break

        scc_num += 1

    return root

for i in range(1, 2 * N + 1):
    if not visit[i]:
        SCC(i)

result = [0] * N
for i in range(1, N + 1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
    if scc_idx[i] < scc_idx[-i]:
        result[i - 1] = 1
else:
    print(1)
    print(*result)


# 2
import sys


input = sys.stdin.readline

stack: list[int] = []
edge_list: list[list[int]]


def initialize(length: int) -> None:
    global _id, scc_id, finished, id_list, sccid_list, edge_list
    _id = 0
    scc_id = 1
    finished = [False for _ in range(length)]
    id_list = [-1 for _ in range(length)]
    sccid_list = [-1 for _ in range(length)]
    edge_list = [[] for _ in range(length)]


def dfs(x: int) -> int:
    global _id, scc_id
    _id += 1
    id_list[x] = _id
    stack.append(x)

    parent: int = id_list[x]
    for nx in edge_list[x]:
        if id_list[nx] == -1:
            parent = min(parent, dfs(nx))
        elif not finished[nx]:
            parent = min(parent, id_list[nx])

    if parent == id_list[x]:
        while True:
            top = stack.pop()
            sccid_list[top] = scc_id
            finished[top] = True
            if top == x:
                break
        scc_id += 1

    return parent


def check(n: int) -> bool:
    for x in range(1, n + 1):
        if sccid_list[x] == sccid_list[-x]:
            return False
    return True


def print_answer(n: int) -> None:
    can_true = check(n)
    print(int(can_true))
    if can_true:
        for x in range(1, n + 1):
            print(int(sccid_list[x] < sccid_list[-x]), end=" ")


def main() -> None:
    n, m = map(int, input().split())

    initialize(2 * n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        edge_list[-x].append(y)
        edge_list[-y].append(x)

    for x in range(1, 2 * n + 1):
        if id_list[x] == -1:
            dfs(x)

    print_answer(n)


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    main()


# 3
from sys import stdin, setrecursionlimit as SRL
input = stdin.readline; SRL(123123)
MIS = lambda: map(int,input().split())

def SCC(adj):
    def dfs(count, v):
        pre[v] = count; count+= 1
        S.append(v); P.append(v)
        for w in adj[v]:
            if pre[w] == -1: count = dfs(count, w)
            elif not scced[w]:
                while P and pre[P[-1]] > pre[w]: P.pop()
        if not P or P[-1] != v: return count
        comp = []
        while S:
            w = S.pop(); scced[w] = True; comp.append(w)
            if w == v: break
        P.pop(); sccs.append(comp)
        return count
    n, count = len(adj), 0
    pre, scced = [-1]*n, [False]*n; S, P, sccs = [], [], []
    for v in range(n//2):
        if pre[v+1] == -1: count = dfs(count, v+1)
        if pre[-v-1] == -1: count = dfs(count, -v-1)
    scx = [-1]*n
    for i in range(len(sccs)):
        for x in sccs[i]: scx[x] = i+1
    return scx, sccs

def TwoSAT(n, cnf):
    adj = [[] for i in range(2*n+1)]
    for a, b in cnf: adj[-a].append(b); adj[-b].append(a)
    scx, res = SCC(adj)
    for i in range(1, n+1):
        if scx[i] == scx[-i]: return False
    assign = [-1]*(n+1)
    for i in range(len(res)-1,-1,-1):
        for var in res[i]:
            if assign[abs(var)] == -1: assign[abs(var)] = var<0
    return assign
                
n, m = MIS()
cnf = []
for i in range(m): cnf.append(tuple(MIS()))
asg = TwoSAT(n, cnf)
if asg == False: print(0)
else:
    print(1)
    print(*map(int, asg[1:]))


# 4
import sys
rd, wt = sys.stdin.readline, sys.stdout.write
sys.setrecursionlimit(10**6)

def scan() : return map(int, rd().split())

def F(node) : return 2 * node if node > 0 else 1 - 2 * node

N, M = scan()

adj = [[] for _ in range(2 * N + 2)]
disc = [-1 for _ in range(2 * N + 2)]
scc = [-1 for _ in range(2 * N + 2)]
ans = [-1 for _ in range(N + 1)]
info, st, num, grp = [], [], 0, 0

def DFS(pre) :

    global num, grp

    disc[pre] = ret = num
    num += 1

    st.append(pre)

    for seq in adj[pre] :
        if disc[seq] < 0 : ret = min(ret, DFS(seq))
        elif scc[seq] < 0 : ret = min(ret, disc[seq])

    if ret == disc[pre] :

        tmp = []
        
        while True :

            node = st.pop()

            scc[node] = grp
            tmp.append(node)

            if node == pre : break

        info.append(tmp)
        grp += 1

    return ret

for _ in range(M) :
    A, B = scan()
    adj[F(-A)].append(F(B))
    adj[F(-B)].append(F(A))

for i in range(2, 2 * N + 2) :
    if disc[i] < 0 : DFS(i)

for i in range(1, N + 1) :
    if scc[2 * i + 1] == scc[2 * i] :
        wt('0')
        sys.exit()

while info :

    arr = info.pop()

    while arr :

        num = arr.pop()

        if ans[num // 2] < 0 : ans[num // 2] = num % 2

wt('1\n')
for i in range(N) : wt('%d ' %ans[i + 1])