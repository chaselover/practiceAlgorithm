from itertools import permutations

N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # iter(tuple)

for i in P:
    print(*i) 