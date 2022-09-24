
N = int(input())
alpha = [0]*26
string = [list(map(lambda x: ord(x)-65,input())) for _ in range(N)]
ans = 0
topN = 9

for i in range(N):
    for m in string[i][::-1]:
        for j in range(len(string[i])):
            alpha[m] += (10**j)
        
alpha.sort(reverse = True)

for i in range(26):
    if alpha[i] ==0:
        continue
    else:
        ans += alpha[i]*topN
        topN -= 1

print(ans)

