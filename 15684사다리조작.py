import sys

input = sys.stdin.readline

def move():
    # 이동을 시작한다. 가능하면 True리턴.
    for i in range(n):
        num = i
        for j in range(h):
            if a[num][j]:
                num += 1
            elif a[num-1][j]:
                num -= 1
        if i != num:
            return 0
    return 1


def dfs(cnt, idx, r):
    global ans
    # 선 갯수 채워지면 이동.
    if cnt == r:
        if move():
            ans = cnt
        return
    # 연결할 선을 탐색.
    for i in range(idx, h):
        for j in range(n-1):
            # 선이 이미 있다면 pass
            if a[j][i]:
                continue
            # 세로선 j의 앞세로선과 뒷세로선에 연결이 있는지 확인.한다.
            if j - 1 >= 0 and a[j-1][i]:
                continue
            if j + 1 < n and a[j+1][i]:
                continue
            #  선 없으면 선넣고 탐색.
            a[j][i] = 1
            dfs(cnt + 1, i, r)
            a[j][i] = 0

n, m, h = map(int, input().split())
# a는 선이 연결되었음을 표시.
a = [[0]*h for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    a[y-1][x-1] = 1

ans, flag = sys.maxsize, 1
for r in range(4):
    dfs(0, 0, r)
    if ans != sys.maxsize:
        print(ans)
        flag = 0
        break
if flag:
    print(-1)

"""
1. 연결을 저장하는 리스트 a를 만든다
    a는 2차 리스트인데 a[세로][가로] 로 사용한다
    따라서 a의 크기는 n x h이다

2. a에 연결 관계를 저장한다
    a[y-1][x-1]은 y-1번째 세로일 때 x-1번째 가로에서 x번째 가로로 이동할 수 있음을 의미한다

3. dfs로 구현한 조합으로 어느 가로선을 연결할 지 정한다

4. dfs에서 연결할 선을 고를 때 다른 가로선과 이어지면 안되는 조건을 고려해야한다
    현재 위치를 세로j , 가로i 라고 할 때 j-1번 째 세로와 j+1번 째 세로에 연결된 가로선이 있는지 확인한다

5. 연결할 가로선을 모두 고르면 move 함수를 실행해서 출발한 세로선과 도착한 세로선의 인덱스가 같은지 확인한다

6. 만일 같으면 ans에 가로선을 고른 개수를 저장하고 return한다

7. ans가 값이 변했으면 ans을 출력하고 종료한다
"""