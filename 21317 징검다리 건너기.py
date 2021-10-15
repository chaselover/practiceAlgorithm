import sys
input = sys.stdin.readline

def dfs(node, energy, key):
    global min_energy
    if energy >= min_energy:
        return
    if node == N:
        min_energy = min(min_energy, energy)
        return
    if node + 1 <= N:
        dfs(node + 1, energy + small_jump[node], key)
    if node + 2 <= N:
        dfs(node + 2, energy + big_jump[node], key)
    if node + 3 <= N and key:
        dfs(node + 3, energy + K, 0)


N = int(input())
big_jump = [0]
small_jump = [0]
for _ in range(N - 1):
    small, big = map(int, input().split())
    small_jump.append(small)
    big_jump.append(big)
K = int(input())
min_energy = float('inf')
dfs(1, 0, 1)
print(min_energy)