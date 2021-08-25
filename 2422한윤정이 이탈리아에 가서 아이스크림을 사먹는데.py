import sys
input = sys.stdin.readline

def dfs(s,cnt):
    global ans
    if cnt==3:
        ans += 1
        return
    if cnt > 3:
        return
    for next in range(s+1,N+1):
        if not eat[next] and next not in donot_list:
            eat[next] = True
            for hate in ice_cream[next]:
                donot_list.append(hate)
            dfs(next, cnt + 1)
            eat[next] = False
            for hate in ice_cream[next]:
                donot_list.pop()

N, M = map(int, input().split())
ice_cream = {i: [] for i in range(1,N+1)}
eat = {i: False for i in range(1,N+1)}
donot_list = []
ice_cream[0] = []
for _ in range(M):
    a,b = map(int, input().split())
    ice_cream[a] += [b]
    ice_cream[b] += [a]
ans = 0
dfs(0,0)
print(ans)



# 민구님 풀이 3개뽑는 총 조합 - 안되는 조합의 수
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# worsts = set()
# for _ in range(M):
#     a, b = map(int, input().split())
#     worst = 1<<(a-1)
#     worst |= 1<<(b-1)
#     for i in range(N):
#         worsts.add(bin(worst|(1<<i)))

# cnt = 0        
# for worst in worsts:
#     if worst.count('1') == 3:
#         cnt = cnt + 1

# print(N*(N-1)*(N-2)//6 - cnt)
