import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = [[0,0,0],[0,0,0]]
min_sum = [[0,0,0],[0,0,0]]
# 슬라이딩 윈도우 N까지 미끄러짐. // dp를 같이 쓰는데 dp를 모두 저장하는 것이 아니라 전의 값과 현재 계산할 칸만 남겨둠.
for i in range(0,N):

    max_sum[1][0] = max(max_sum[0][1], max_sum[0][0]) + arr[i][0]
    max_sum[1][1] = max(max_sum[0][1], max_sum[0][2], max_sum[0][0]) + arr[i][1]
    max_sum[1][2] = max(max_sum[0][1], max_sum[0][2]) + arr[i][2]

    min_sum[1][0] = min(min_sum[0][0], min_sum[0][1]) + arr[i][0]
    min_sum[1][1] = min(min_sum[0][1], min_sum[0][2], min_sum[0][0]) + arr[i][1]
    min_sum[1][2] = min(min_sum[0][1], min_sum[0][2]) + arr[i][2]

    max_sum.append(max_sum.pop(0))
    min_sum.append(min_sum.pop(0))

print(max(max_sum[0]), min(min_sum[0]))

# 아래도 동일한 방식이나 한줄에 연산을 해 값이 바뀌는것을막음(tmp배열을 쓰지 않도록 설계 이전값 없이 현재값에 계속 최신화 하게끔 함.)
# import sys
# input = sys.stdin.readline
# n = int(input())
# s = [list(map(int, input().split())) for i in range(n)]
# lax, cax, rax = s[0][0], s[0][1], s[0][2]
# lin, cin, rin = s[0][0], s[0][1], s[0][2]
# for i in range(1, n):
#     lax, cax, rax = max(lax, cax) + s[i][0], max(lax, cax, rax) + s[i][1], max(cax, rax) + s[i][2]
#     lin, cin, rin = min(lin, cin) + s[i][0], min(lin, cin, rin) + s[i][1], min(cin, rin) + s[i][2]
# print(max(lax, cax, rax), min(lin, cin, rin))