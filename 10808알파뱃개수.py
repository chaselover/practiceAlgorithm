
S = input()
alpha = [0]*26

for ch in S:
    alpha[ord(ch)-ord('a')] += 1

for i in alpha:
    print(i,end=" ")