from math import factorial

T = int(input())
for test in range(T):
    N,M = map(int,input().split())
    
    answer = factorial(M)//(factorial(N)*factorial(M-N))
    print(answer)