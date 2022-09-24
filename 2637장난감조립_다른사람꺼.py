def get_parts(part):
    # part 를 만들기 위해 필요한 기본 부품 dictionary 반환
    if chk[part]:
        return need[part]
    target_cnt = {}
    for need_item, need_cnt in need[part].items():  # need_item: part을 만들기 위해 필요한 부품 / need_cnt: 필요한 부품 갯수
        if len(need[need_item]) == 0:  # 기본 부품일 경우 (i를 만드는데에 필요한 부품이 없다)
            if need_item in target_cnt:
                target_cnt[need_item] += need_cnt
            else:
                target_cnt[need_item] = need_cnt
            continue
        for k, v in get_parts(need_item).items():  # get(need_item) : need_item를 만드는데에 필요한 부품들
            if k in target_cnt:
                target_cnt[k] += v * need_cnt
            else:
                target_cnt[k] = v * need_cnt
    need[part] = target_cnt
    chk[part] = True
    return target_cnt


N = int(input())
M = int(input())
need = {i: {} for i in range(1, N + 1)}  # need[a][b] = c : a를 만드는데에 b가 c개 필요하다
chk = {i: True for i in range(1, N + 1)}  # chk[a] = True
for _ in range(M):
    X, Y, K = map(int, input().split())
    need[X][Y] = K
    chk[X] = False

ans = get_parts(N)
for i in range(1, N):
    if i in ans:
        print(i, ans[i])
