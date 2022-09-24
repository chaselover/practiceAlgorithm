# 인접 행렬로 구현한 다익스트라 코드
import sys


def dijkstra(K, V, graph):
    INF = sys.maxsize
    # s는 해당 노드를 방문 했는지 여부를 저장하는 변수이다
    s = [False] * V
    # d는 memoization을 위한 array이다. d[i]는 정점 K에서 i까지 가는 최소한의 거리가 저장되어 있다.
    d = [INF] * V
    d[K - 1] = 0

    while True:
        m = INF
        N = -1

        # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
        # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j

        # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
        # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.
        if m == INF:
            break

        # N번 노드를 '방문'한다.
        # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는 노드가 있는지 확인하고,
        # 더 빨리 갈 수 있다면 해당 노드(노드의 번호 j라고 하자)의 d[j]를 업데이트 해준다.
        s[N] = True

        for j in range(V):
            if s[j]: continue
            via = d[N] + graph[N][j]
            if d[j] > via:
                d[j] = via

    return d

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    INF = sys.maxsize
    graph = [[INF]*V for _ in range(V)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u-1][v-1] = w

    for d in dijkstra(K, V, graph):
        print(d if d != INF else "INF")