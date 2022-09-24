def GCD(i,j):
    a, b = i,j
    
    
    while b != 0: 
        a = a % b 
        a, b = b, a 
    return a

N,S =  map(int,input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i]>=S:
        A[i] = A[i]-S
    else:
        A[i] = S-A[i]

init_GCD = A[0]

for i in range(1,N):
    init_GCD = GCD(init_GCD,A[i])

print(init_GCD)