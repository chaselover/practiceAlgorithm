def GCD(i,j):
    a, b = i,j
    
    
    while b != 0: 
        a = a % b 
        a, b = b, a 
    return a

t = int(input())

for test in range(t):
    n = list(map(int,input().split()))
    ans = 0
    for i in range(1,n[0]):
        for j in range(i+1,n[0]+1):
            ans += GCD(n[i],n[j])
    print(ans)