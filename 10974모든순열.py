from itertools import permutations

N = int(input())

permutation_s = permutations(range(1,N+1))
for x in permutation_s:
    print(*x)