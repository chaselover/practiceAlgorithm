import sys

input = sys.stdin.readline

n = int(input())
sharks = []
for _ in range(n):
    # 크기 속도 지능
    sharks.append(list(map(int, input().strip().split())))
destination = n + n + 1
one_des = destination + 1
graph = dict([(i, {}) for i in range(one_des)])
for i, eat in enumerate(sharks):
    eat_index = i + 1
    graph[0][eat_index] = 2
    for j, food in enumerate(sharks):
        food_index = n + j + 1
        if i == j:
            continue
        else:
            if eat[0] >= food[0] and eat[1] >= food[1] and eat[2] >= food[2]:
                if eat[0] == food[0] and eat[1] == food[1] and eat[2] == food[2]:
                    if i > j:
                        graph[eat_index][food_index] = 1
                else:
                    graph[eat_index][food_index] = 1
for i in range(n + 1, destination):
    graph[i][destination] = 1


def search(current):
    visit[current] = 1
    use_graph = graph[current]

    for e in use_graph:
        # e - 연결된 그래프의 노드 use_graph[e] - 웨이트
        # 0이 되면 제거하기로 하자 -> 0이 있다면 0이 되는지도 체크
        if visit[destination] == 1:
            return 1
        if visit[e] == 1:
            continue
        else:
            parent[e] = current
            search(e)


# 경로를 찾을 수 없을 때 멈추기
while True:
    visit = [0 for _ in range(one_des)]
    parent = [None for _ in range(one_des)]
    search(0)
    if visit[destination] == 0:
        break
    end = destination
    while True:
        pa = parent[end]
        if pa == None:
            break

        if graph[pa][end] == 1:
            del graph[pa][end]
        else:
            graph[pa][end] -= 1
        if pa != 0:
            try:
                graph[end][pa] += 1
            except:
                graph[end][pa] = 1
        end = pa
print(n - len(graph[destination]))