import sys 
input = sys.stdin.readline

N, T = map(int, input().split()) 
w_ps = [list(map(int, input().split())) for _ in range(N)] 
w_ps.sort(key = lambda x: x[1],reverse=True)

answer = 0
for w, p in w_ps: 
    answer += (w + p*(T-1)) 
    T -= 1 
print(answer)

