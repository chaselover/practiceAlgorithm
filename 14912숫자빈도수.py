from collections import Counter

n,d = input().split()
n_list = ''.join(map(str,list(range(1,int(n)+1))))
b = Counter(n_list)
print(b[d])