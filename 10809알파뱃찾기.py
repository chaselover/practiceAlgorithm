
S = input()
alpha = [-1]*26

for i in range(len(S)):
    if(alpha[ord(S[i])-ord('a')] == -1):
        alpha[ord(S[i])-ord('a')] = i

for i in alpha:
    print(i,end=" ")