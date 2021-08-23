import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
stone = input().rstrip()
# 까만색 B개 이하, 흰색은W개 이상
left = 0
w_cnt = 0
b_cnt = 0
max_len = 0
for right in range(N):
    if stone[right]=='W':
        w_cnt += 1
    else:
        b_cnt += 1
    while b_cnt > B:
        if stone[left]=='W':
            w_cnt -= 1
        else:
            b_cnt -= 1
        left += 1
    if w_cnt>=W:
        max_len = max(max_len,right-left+1)
print(max_len)