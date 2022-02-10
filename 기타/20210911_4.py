
def make_sieve(n):
    primes = [True,True] + [False]*(n-1)
    m = int(n**0.5)+1
    for i in range(2,m):
        if not primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = True
    return [num for num in range(n+1) if not primes[num]]


def divied_conquer(arr, size):
    if size == 1:
        return arr
    for num in prime_nums:
        if not size%num:
            pivot = num
            break
    conquer = []
    for start in range(pivot):
        conquer += divied_conquer([arr[i] for i in range(start,size,pivot)],size//pivot)
    return conquer

    
def solution(n):
    global prime_nums
    arr = [i for i in range(1,n+1)]
    prime_nums = make_sieve(n)
    ans = divied_conquer(arr,n)
    return ans
print(solution(1000000))