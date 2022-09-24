system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
B = int(B)
N = list(N)
ans = 0
i=0

while N:
    ans += system.find(N.pop())*(B**i)
    i += 1
    
print(ans)