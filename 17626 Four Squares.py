import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append((n,0))
    visited[n] = True
    while q:
        r, cnt = q.popleft()
        flag = 1
        for square in squares:
            next_r = r-square
            if next_r > 0 and not visited[next_r]:
                if flag:
                    first = next_r
                    flag = 0
                if first > square and next_r>=4:
                    break
                visited[next_r] = True
                q.append((next_r,cnt+1))
            elif next_r == 0:
                return cnt + 1
                
n = int(input())
squares = []
m = int(50000*0.5)
for i in range(m,0,-1):
    squares.append(i**2)
visited = {i: False for i in range(n+1)}
print(bfs(n))



###1등코드:
# class Solution:
# 	def sq(self, n):
# 		x = int(n**0.5)
# 		return x*x == n
# 	def Nsq(self, n):
# 		if n < 4: return n
# 		if self.sq(n): return 1
# 		while n & 3 == 0:
# 			n >>= 2
# 		if n & 7 == 7: return 4
# 		x = int(n**0.5)
# 		for i in range(1, x+1):
# 			if self.sq(n - i*i): return 2
# 		return 3
# X = Solution(); N = int(input())
# print(X.Nsq(N))