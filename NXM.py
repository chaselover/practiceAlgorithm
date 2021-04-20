N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    # 주어진 개수만큼 채워지면 출력한다
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
        
        # i번째는 거쳐갈거라서 True로 바꾼다.
        check_list[i] = True
        arr.append(num_list[i])
        # 현재의 i를 기준으로 가지치기 시작
        dfs(cnt + 1)
        # 이 부분은
        arr.pop()
        # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
        print(arr)
        print(check_list)
        check_list[i] = False
        
dfs(0)