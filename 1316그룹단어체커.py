import sys
input = sys.stdin.readline
N = int(input())
cnt=0
for _ in range(N):
    chr_set = {i:0 for i in range(97,123)}
    word = input().rstrip()
    for i in range(len(word)):
        if chr_set[ord(word[i])]==1:
            break
        if i<len(word)-1 and word[i] != word[i+1]:
            chr_set[ord(word[i])]=1
    else:
        cnt+=1
print(cnt)
    