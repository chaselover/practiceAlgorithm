SIZE = 500000

N = int(input())
blocks = list(map(int,input().split()))
dp = [-1] * SIZE

dp[0] = 0
for block_h in blocks:
	next_dp = dp[:]
	for h in range(SIZE):
		if dp[h] < 0:
			continue
		# to min
		next_h = abs(h - block_h)
		next_value = dp[h] + min(h, block_h)
		if next_h < SIZE:
			next_dp[next_h] = max(next_dp[next_h], next_value)
		# to max
		next_h = h + block_h
		next_value = dp[h]
		if next_h < SIZE:
			next_dp[next_h] = max(next_dp[next_h], dp[h])
	dp = next_dp

if dp[0] == 0:
	print(-1)
else:
	print(dp[0])


from sys import stdin

n = int(stdin.readline())
blocks = list(map(int, stdin.readline().split()))
dp = [0 for _ in range(500001)]
ans = -1

for i in range(n) :
  temp = dp[:]
  for j in range(500001):
    if dp[j] or j==0:
      if dp[j] + blocks[i] > temp[j + blocks[i]] : # 쌓은 블럭이 그 전 높이차이 최대 탑 높이보다 클 경우
        temp[j + blocks[i]] = dp[j] + blocks[i]

      if j > blocks[i] :
        if dp[j] > temp[j - blocks[i]] :
          temp[j - blocks[i]] = dp[j]

      elif j < blocks[i] :
        if blocks[i] + dp[j] - j > temp[blocks[i] - j]:
          temp[blocks[i] - j] = blocks[i] + dp[j] - j

      else :
        if temp[0] < dp[j] :
          temp[0] = dp[j]
        if ans < dp[j] : ans = dp[j]
  dp = temp[:]

print(ans)


import sys
input = sys.stdin.readline

n = int(input())
block = list(map(int, input().split()))

if n == 1:
    print(-1)
    quit()
height_sum = sum(block)
dp = [[-1] * height_sum for _ in range(len(block))]
dp[0][0] = 0
dp[0][block[0]] = block[0]
for i in range(len(block) - 1):
    for j in range(height_sum//2 + 1):
        # i+1번째 블록을 사용하지 않는 경우
        if dp[i][j] != -1:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            # 더 높은 탑에 쌓는 경우
            if j + block[i + 1] < height_sum:
                dp[i + 1][j + block[i + 1]] = max(dp[i + 1][j + block[i + 1]], dp[i][j] + block[i + 1])
            # 더 낮은 탑에 쌓는 경우 case1. block_i <= j case2. block_i > j
            if block[i + 1] <= j:
                dp[i + 1][j - block[i + 1]] = max(dp[i + 1][j - block[i + 1]], dp[i][j])
            else:
                dp[i + 1][block[i + 1] - j] = max(dp[i + 1][block[i + 1] - j], dp[i][j] + block[i + 1] - j)
if dp[-1][0] == 0:
    print(-1)
else:
    print(dp[-1][0])


