

N,K = map(int,input().split())
coins = []
cnt = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(1,N):
   cnt += K // coins[-i]
   K = K % coins[-i]
    
print(cnt)
    
    