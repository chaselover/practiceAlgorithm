import sys
input = sys.stdin.readline

def change(now, cnt): 
    if cnt == 1: 
        now[0] ^= 1
        now[1] ^= 1
    for i in range(1, n-1): 
        if now[i-1] != target[i-1]: 
            cnt += 1 
            now[i-1] ^= 1
            now[i] ^= 1 
            now[i+1] ^= 1 
    if now[n-2] != target[n-2]:
        cnt += 1 
        now[n-2] ^= 1
        now[n-1] ^= 1
    return cnt if now == target else float('inf')


n = int(input()) 
now = list(map(int, input().rstrip())) 
target = list(map(int,input().rstrip())) 
res1 = change(now[:], 0) 
res2 = change(now[:], 1) 
print(min(res1, res2) if res1 != float('inf') or res2 != float('inf') else -1) 

