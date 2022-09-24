def solution(users, emoticons):
    global max_cnt, max_buying
    max_cnt, max_buying = 0, 0
    
    def dfs(depth, comb_percents):
        global max_cnt, max_buying
        if depth == len(emoticons):
            cnt = 0
            total_buying = 0
            for user in users:
                buying = 0
                for idx, percent in enumerate(comb_percents):
                    if user[0] <= percent:
                        buying += (emoticons[idx] * (100 - percent)) // 100
                if buying >= user[1]:
                    cnt += 1
                else:
                    total_buying += buying
            if cnt > max_cnt:
                max_cnt = cnt
                max_buying = total_buying
            elif cnt == max_cnt and total_buying > max_buying:
                max_buying = total_buying
            return
        for percent in [10, 20, 30, 40]:
            dfs(depth + 1, comb_percents + [percent])
    
    dfs(0, [])
    return [max_cnt, max_buying]
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))