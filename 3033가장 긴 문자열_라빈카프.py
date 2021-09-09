# Suffix array와 LCP
import sys
global n, texts, mod
n = int(sys.stdin.readline().rstrip())
texts = sys.stdin.readline().rstrip()
mod = 999983
base = 31
n_table = []
n_table.append(1)
for i in range(1,n):
    n_table.append(n_table[i-1] * base % mod)

def pattern_match(idx1, idx2, M):
    global texts
    for i in range(M):
        if texts[idx1+i] != texts[idx2+i]: return False
    return True


result = 0
def check(length):
    global n, texts, mod
    hash_table = {}
    num = n - length + 1
    h = 0
    for i in range(length):
        h *= base
        h += ord(texts[i])
        h %= mod
    hash_table[h] = [0]
    for i in range(1,num):
        h -= ord(texts[i-1])*n_table[length-1] % mod
        h = h % mod
        h *= base
        h += ord(texts[i+length-1])
        h %= mod
        if hash_table.get(h):
            for h_t in hash_table[h]:
                if pattern_match(i,h_t,length):
                    return True
            hash_table[h].append(i)
        else:
            temp_lst = [i]
            hash_table[h] = temp_lst
    return False

low = 0
high = n-1
result = 0
while low <= high: 
    mid = int((low+high)/2)
    if check(mid):
        result = mid
        low = mid + 1
    else:
        high = mid -1

print(result)



#############################################################################
P = 31
M = [1000000009, 1234567891]

l = int(input())
string = input()

def powmod(a, b, m):
    if b == 0:
        return 1
    x = powmod(a, b//2, m)
    return x*x*a%m if b%2 else x*x%m

invs = [powmod(P, x-2, x) for x in M]

s, e = 0, len(string)-1
while s < e:
    m = (s + e + 1) // 2
    hashset = set()
    hasduplicate = False

    hashval, c = [0, 0], [1, 1]
    for i in range(m):
        for j in range(len(M)):
            hashval[j] += (ord(string[i])-ord('a')) * c[j]
            hashval[j] %= M[j]
            c[j] *= P
            c[j] %= M[j]
    hashset.add(tuple(hashval))

    for i in range(l-m):
        for j in range(len(M)):
            hashval[j] += (ord(string[i+m])-ord('a')) * c[j]
            hashval[j] -= (ord(string[i])-ord('a'))
            hashval[j] *= invs[j]
            hashval[j] %= M[j]
        if tuple(hashval) in hashset:
            hasduplicate = True
            break
        hashset.add(tuple(hashval))
    
    if hasduplicate:
        s = m
    else:
        e = m - 1

print(s)



#############################################################################
# Problem No.: 3033
# Solver:      Jinmin Goh
# Date:        20200621
# URL: https://www.acmicpc.net/problem/3033

import sys
import collections

def main():
    n = int(input())
    S = input()

    # appropriate prime
    modVal = 2147483647
    powVal = 256

    def RabinKarp() -> bool:
        if pMid == 0:
            return True
        tempVal = 0
        for i in range(pMid):
            tempVal = (tempVal * powVal + ord(S[i])) % modVal

        mulVal = (1 << (8 * (pMid - 1))) % modVal
                    
        hashDict = collections.defaultdict(list)
        hashDict[tempVal].append(0)
        
        for i in range(len(S) - pMid):
            tempVal = ((tempVal - ord(S[i]) * mulVal) * powVal + ord(S[i + pMid])) % modVal
            for j in hashDict[tempVal]:
                if S[i + 1:i + pMid + 1] == S[j:j + pMid]:
                    return True
            hashDict[tempVal].append(i + 1)
        return False

    # binary search
    pFront = 0
    pRear = len(S)
    while pFront + 1 < pRear:
        pMid = (pFront + pRear) // 2    
        flag = RabinKarp()
        if flag:
            pFront = pMid
        else:
            pRear = pMid
    print(pFront)
    return

if __name__ == "__main__":
    main()



#############################################################################
n = int(input())
s = input()

r = [ord(i) for i in s]
sa = [i for i in range(n)]
tmp = [0] * n
lcp = [-1] * n 
f = lambda m: r[m] if m<n else -1

L = 1
while L <= n:
  sa.sort(key=lambda x: (f(x), f(x+L)))

  rnk = 0
  tmp[sa[0]] = rnk

  for i in range(1, n):
    if f(sa[i]) != f(sa[i-1]) or f(sa[i]+L) != f(sa[i-1]+L):
      rnk += 1
    tmp[sa[i]] = rnk 

  r = tmp[:]
  L <<= 1

for i in range(n):
  r[sa[i]] = i

ans = 0

L = 0
for i in range(n):
  if r[i]:
    j = sa[r[i] - 1]

    while i+L<n and j+L<n and s[i+L] == s[j+L]:
      L += 1
    
    lcp[r[i]] = L 
    ans = max(ans, L)

    L = L-1 if L else 0 

print(ans)