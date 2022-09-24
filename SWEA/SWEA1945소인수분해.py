for test in range(1, int(input())+1):
    N = int(input())
    prime_nums = [2, 3, 5, 7, 11]
    answer_arr = []
    for num in prime_nums:
        cnt = 0
        while not N % num:
            N = N//num
            cnt += 1
        answer_arr.append(cnt)
    print(f'#{test}',end=" ")
    print(*answer_arr)