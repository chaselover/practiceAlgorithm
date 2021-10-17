def suffix_array_IS(str, str_o:int, str_n:int, str_k:int, suffix):
    t = [False] * str_n
    t[str_n-2] = False
    t[str_n-1] = True

    for i in range(str_n-3, -1, -1):
        t[i] = str[str_o+i] < str[str_o+i+1] or t[i+1] and str[str_o+i] == str[str_o+i+1]

    bkt = [False] * (str_k+1)
    suffix_array_get_buckets(str, str_o, str_n, str_k, bkt, True)

    for i in range(str_n): suffix[i] = -1
    for i in range(1, str_n):
        if t[i] and not t[i-1]:
            bkt[str[str_o+i]] -= 1
            suffix[bkt[str[str_o+i]]] = i
    
    suffix_array_induce_suffix_L(t, suffix, str, str_o, str_n, str_k, bkt, False)
    suffix_array_induce_suffix_R(t, suffix, str, str_o, str_n, str_k, bkt, True)

    n1 = 0
    for i in range(str_n):
        si = suffix[i]
        if si > 0 and t[si] and not t[si-1]:
            suffix[n1] = suffix[i]
            n1 += 1

    for i in range(n1, str_n): suffix[i] = -1
    name, prev = 0, -1
    for i in range(n1):
        pos = suffix[i]
        diff = False
        for d in range(str_n):
            if prev == -1 or str[str_o+pos+d] != str[str_o+prev+d] or t[pos+d] != t[prev+d]:
                diff = True
                break
            elif d > 0:
                pd = pos+d
                if pd > 0 and t[pd] and not t[pd-1]: break
                pd = prev+d
                if pd > 0 and t[pd] and not t[pd-1]: break
        if diff:
            name += 1
            prev = pos
        pos //= 2
        suffix[n1+pos] = name-1
    j = str_n-1
    for i in range(str_n-1, n1-1, -1):
        if suffix[i] >= 0:
            suffix[j] = suffix[i]
            j -= 1
    if name < n1:
        suffix_array_IS(suffix, str_n-n1, n1, name-1, suffix)
    else:
        for i in range(n1):
            suffix[suffix[str_n-n1+i]] = i

    suffix_array_get_buckets(str, str_o, str_n, str_k, bkt, True)
    j = 0
    for i in range(1, str_n):
        if t[i] and not t[i-1]:
            suffix[str_n-n1+j] = i
            j += 1
    for i in range(n1): suffix[i] = suffix[str_n-n1+suffix[i]]
    for i in range(n1, str_n): suffix[i] = -1
    for i in range(n1-1, -1, -1):
        j = suffix[i]
        suffix[i] = -1
        bkt[str[str_o+j]] -= 1
        suffix[bkt[str[str_o+j]]] = j
    
    suffix_array_induce_suffix_L(t, suffix, str, str_o, str_n, str_k, bkt, False)
    suffix_array_induce_suffix_R(t, suffix, str, str_o, str_n, str_k, bkt, True)

def suffix_array_get_buckets(str, str_o:int, str_n:int, str_k:int, bkt, end:bool):
    for i in range(str_k+1): bkt[i] = 0
    for i in range(str_n): bkt[str[str_o+i]] += 1
    s = 0
    for i in range(str_k+1):
        s += bkt[i]
        if end: bkt[i] = s
        else: bkt[i] = s - bkt[i]

def suffix_array_induce_suffix_L(t, suffix, str, str_o:int, str_n:int, str_k:int, bkt, end:bool):
    suffix_array_get_buckets(str, str_o, str_n, str_k, bkt, end)
    for i in range(str_n):
        j = suffix[i] - 1
        if j >= 0 and not t[j]:
            suffix[bkt[str[str_o+j]]] = j
            bkt[str[str_o+j]] += 1

def suffix_array_induce_suffix_R(t, suffix, str, str_o:int, str_n:int, str_k:int, bkt, end:bool):
    suffix_array_get_buckets(str, str_o, str_n, str_k, bkt, end)
    for i in range(str_n-1, -1, -1):
        j = suffix[i] - 1
        if j >= 0 and t[j]:
            bkt[str[str_o+j]] -= 1
            suffix[bkt[str[str_o+j]]] = j

class SuffixArray:
    """ 주어진 문자열 s에 대한 접미사 배열과 LCP 배열을 계산한다. """

    str = []

    suffix = []
    """ 접미사 배열. 접미사의 시작 지점을 비교하여 문자열이 앞선 순으로 저장되어 있음. 맨 처음은 항상 빈 문자열임. """
    suffix_pos = []
    """ 접미사의 시작 지점이 주어졌을 때, suffix 배열의 몇 번째 원소인지를 저장하고 있음. `suffix_pos[suffix[i]] == i` """
    lcp = []
    """ `suffix[i]`와 `suffix[i+1]` 사이 공통된 접두사의 길이를 저장하고 있음. """

    def __init__(self, s:str):
        self._alphabets = [''] + sorted(list(set(c for c in s)))
        self._alphabets_lookup = dict()
        for (i, c) in enumerate(self._alphabets): self._alphabets_lookup[c] = i

        self.str = [self._alphabets_lookup[c] for c in s] + [0]
        l = len(self.str)

        self._len = l

        if l > 0:
            self._compute_suffix_array()

            self.suffix_pos = [0] * l
            self.lcp = [0] * l

            for i in range(l): self.suffix_pos[self.suffix[i]] = i
            self._compute_lcp_array()

    def __len__(self):
        return self._len-1

    def _compute_suffix_array(self):
        self.suffix = [-1] * self._len
        suffix_array_IS(self.str, 0, self._len, len(self._alphabets), self.suffix)

    def _compute_lcp_array(self):
        k = 0
        l = self._len
        for i in range(l):
            if self.suffix_pos[i] == l-1: continue
            j = self.suffix[self.suffix_pos[i]+1]
            max_k = l - max(i, j)
            while k < max_k and self.str[i+k] == self.str[j+k]: k += 1
            self.lcp[self.suffix_pos[i]] = k
            k = max(k-1, 0)

# main code

arr = SuffixArray(input())
print(' '.join((str(i + 1) for i in arr.suffix[1:])))
print('x', ' '.join((str(i) for i in arr.lcp[1:-1])))


# 풀이2
import sys
sys.setrecursionlimit(9990000)
import collections

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    print(mid)
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if cmp(left[0], right[0]):
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def cmp(i,j):
    if pos[i] != pos[j]:
        return pos[i] < pos[j]
    i+=d
    j+=d
    if i<l and j<l:
        return pos[i] < pos[j]
    else:
        return i>j


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    pos_pivot = pos[pivot]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if pos[num] < pos_pivot:
            lesser_arr.append(num)
        elif pos[num] > pos_pivot:
            greater_arr.append(num)
        else:
            if num+d <l and pivot+d<l:
                if pos[num+d]<pos[pivot+d]:
                    lesser_arr.append(num)
                elif pos[num+d]>pos[pivot+d]:
                    greater_arr.append(num)
                else:
                    equal_arr.append(num)
            elif num+d > pivot+d :
                lesser_arr.append(num)
            elif pivot+d > num+d:
                greater_arr.append(num)
            else:
                equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

s = sys.stdin.readline().replace('\n','')
l = len(s)
#pos = collections.deque([-1]*l)
#sa = collections.deque([-1]*l)
pos = [-1]*l
sa = [-1]*l


for i in range(l):
    sa[i] = i
    pos[i] = s[i]

d = 1
while d<=l:
    sa = quick_sort(sa)
    #print(sa)
    temp=[0]*l
    for i in range(l-1):
        temp[i+1] = temp[i] + cmp(sa[i], sa[i+1])
    for i in range(l):
        pos[sa[i]] = temp[i]
    if temp[l-1]==l-1: break
    d*=2

lcp = ['x']*l

k = 0
#print(sa, pos)

for i in range(l):
    k = max(k-1, 0)
    if pos[i] == l-1: continue
    j = sa[pos[i]+1]
    #print(i, j, pos[i], pos[j], sa[i], sa[j])
    while i+k < l and j+k < l and s[i+k] == s[j+k]:
        #print(s[i+k], s[j+k])
        k += 1
    lcp[pos[i]] = k
    #print(k)

for i in range(l):
    sa[i]=sa[i]+1
print(' '.join(map(str, sa)))
#print(*sa)
#print(' '.join(map(str, pos)))
print('x '+' '.join(map(str, lcp[:-1])))



# 3
from sys import stdin
import time
from functools import cmp_to_key

def compare_sa():
    for i in range(n-1):
        for j in range(0,n-i-1):
            swap = False
            if pos[sa[j]] != pos[sa[j+1]]:
                if pos[sa[j]] > pos[sa[j+1]]:
                        swap =True
            else:
                if sa[j]+d <n and sa[j+1]+d <n : #범위 안이라면
                    if pos[sa[j]+d] > pos[sa[j+1]+d]:
                        swap =True
                else:
                    if sa[j] < sa[j+1]:
                        swap =True
            if swap:
                sa[j],sa[j+1] = sa[j+1],sa[j]

def cmp(i,j):
    if pos[i] != pos[j]:
        return pos[i] - pos[j]
    i += d
    j += d
    if i <n and j <n :
        return pos[i] - pos[j]
    else:
        return j - i


def getGroup(x):
        if x < n:
            return pos[x]
        else:
            return -1


def LCP():
    k=0
    for i in range(0,n):
        if pos[i] == n-1 : continue;
        j = sa[pos[i]+1]
        while(1):
            if i+k < n and j+k < n and s[i+k] == s[j+k]:
                k += 1
            else:
                break
        lcp[pos[i]+1]=k
        k = max(k-1,0)
            
        
s = str(stdin.readline().rstrip())
# s = 'a'*200000

# start = time.time()

n = len(s)
sa =[i for i in range(n)]
pos = [ord(s[i]) for i in range(n)]
lcp = ['x']*n

d=1
while(1):
    # compare_sa()
    sa.sort(key=lambda x: (getGroup(x), getGroup(x + d)))
    # sa.sort(key=cmp_to_key(cmp))
    #그룹 지정
    temp = [0]*n
    for i in range(n-1):
        if cmp(sa[i],sa[i+1]) < 0:
            temp[i+1] = temp[i] + 1
        else:
            temp[i+1] = temp[i]

    for i in range(n):
        pos[sa[i]] = temp[i]

    if temp[n-1] == n-1:
        break
    d = 2*d

LCP()

for i in range(n):
    sa[i] += 1

print(*sa)
print(*lcp)


# 5
def get_suffix_array(s, n):
    suffix_array = [i for i in range(n)]
    group = [ord(s[i]) for i in range(len(s))]
    new_group = [0] * n

    def getGroup(x):
        if x < n:
            return group[x]
        else:
            return -1

    t = 1
    while t < n:
        suffix_array.sort(key=lambda x: (getGroup(x), getGroup(x + t)))
        new_order = 0
        new_group[suffix_array[0]] = 0

        for i in range(1, n):
            x = suffix_array[i - 1]
            y = suffix_array[i]

            if getGroup(x) != getGroup(y) or getGroup(x+t) != getGroup(y+t):
                new_order += 1
            new_group[y] = new_order

        group = new_group[:]
        t <<= 1
    return suffix_array

def get_lcp(sfx, n):
    lcp = [0] * n
    rank = [0] * n

    for i in range(n):
        rank[sfx[i]] = i

    length = 0
    for i in range(n):
        k = rank[i]
        if k != 0:
            j = sfx[k-1]
            while j + length < n and s[j + length] == s[i + length]:
                length += 1
            lcp[k] = length
            if length:
                length -= 1

    return lcp

def get_lcs(sfx, lcp, na):
    lcs_start = 0
    lcs_length = 0

s = input()

n = len(s)

sfx = get_suffix_array(s, n)
lcp = get_lcp(sfx, n)
lcp[0] = 'x'
print(" ".join(map(lambda x : str(x+1), sfx)))
print(" ".join(map(str, lcp)))


# 6 숏코드
s = input()

n = len(s)

r = [ord(i) for i in s]
sa = [i for i in range(n)]
tmp = [0] * n
lcp = ['x'] * n  
f = lambda x: r[x] if x < n else -1

L = 1 
while L <= n:
  sa.sort(key=lambda x: (f(x), f(x+L)))

  rank = 0
  tmp[sa[0]] = rank

  for i in range(1, n):
    if f(sa[i]) != f(sa[i-1]) or f(sa[i]+L) != f(sa[i-1]+L):
      rank += 1
    tmp[sa[i]] = rank 

  r = tmp[:]
  L <<= 1


for i in range(n):
  r[sa[i]] = i

L = 0
for i in range(n):
  L = L-1 if L else L

  if r[i]:
    j = sa[r[i] - 1]
    
    while i+L<n and j+L<n and s[i+L] == s[j+L]:
      L += 1

    lcp[r[i]] = L

print(*[i+1 for i in sa])
print(*lcp)