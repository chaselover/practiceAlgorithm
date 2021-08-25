from collections import deque

for _ in range(10):
    test = int(input())
    arr = deque(list(map(int, input().split())))
    cnt = 0
    while arr[-1] > 0:
        arr.rotate(-1)
        arr[-1] -= cnt%5+1
        cnt += 1
    arr[-1] = 0
    print(f'#{test}',*arr)


# for _ in range(10):
#     test = int(input())
#     arr = list(map(int, input().split()))
#     idx = -1
#     cnt = 0
#     while arr[idx] > 0:
#         idx += 1
#         idx %= 8
#         arr[idx] -= cnt % 5 + 1
#         cnt += 1
#     arr[idx] = 0
#     answer = arr[idx+1:] + arr[:idx+1]
#     print(f'#{test}', *answer)