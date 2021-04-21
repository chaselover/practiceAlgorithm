ans = []
N = list(input().split())
for j in range(2):
    n = list(N[j])
    string = ''
    for i in range(2,-1,-1):
        string += n[i]
    ans.append(int(string))

print(max(ans))