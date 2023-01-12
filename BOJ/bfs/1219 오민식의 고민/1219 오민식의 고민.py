def check(E):
    visit = [0] * N
    q = [E]
    while q:
        a = q.pop()
        if a == End:
            return True
        visit[a] = 1
        for b, c in network[a]:
            if visit[b] == 0:
                q.append(b)
    return False


def BF():
    for i in range(N+1):
        if sections[End] == -float('inf') and i == N:
            print('gg')
            return
        for j in range(N):
            if sections[j] == -float('inf'):
                continue
            for E, T in network[j]:
                if sections[j] + T > sections[E]:
                    sections[E] = sections[j] + T
                    if i == N:
                        if check(E):
                            print('Gee')
                            return False
    return True


N, Start, End, M = map(int, input().split())
sections = [-float('inf')] * N
network = [[] for i in range(N)]
for i in range(M):
    S, E, T = map(int, input().split())
    network[S].append([E, T])
salary = list(map(int, input().split()))
sections[Start] = salary[Start]
for i in range(len(salary)):
    for j in range(len(network[i])):
        for k in range(len(salary)):
            if network[i][j][0] == k:
                network[i][j][1] = salary[k] - network[i][j][1]

if BF():
    print(sections[End])