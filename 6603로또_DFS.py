def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
        # s[0]을 첫번째에 넣고 s[1]을 두번째에 넣고...dfs로 파고들면서 depth가 완성되면 하나 출력, 줄바꾸고 s[i]가 쭉쭉 밀리다가 depth 6을 더이상
        # 유지 하지 못할 순간이 오면 (dfs마다 start가 점점 늘어나기 때문에 남은 숫자가 6개 미만이 되면 답을 낼 수 없다.) 더이상 출력없이 dfs가 종료.
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)

combi = [0 for _ in range(13)]

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()