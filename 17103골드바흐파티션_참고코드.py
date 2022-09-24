prime_arr = []

# sieve = 체
sieve = [False, False] + ([True] * (1000000 - 1))
for i in range(2, 1000001):
    if sieve[i]:
        prime_arr.append(i)
    for j in range(i * 2, 1000001, i):
        sieve[j] = False

ans = []
for tc in range(int(input())):
 
    N = int(input())
    cnt = 0
    for i in range(len(prime_arr)):
        if prime_arr[i] > N - prime_arr[i]:
            break
        if sieve[N - prime_arr[i]]:
            cnt += 1
    ans.append(cnt)

print(*ans, sep='\n')