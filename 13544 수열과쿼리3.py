#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def main():
    N = int(input())
    a = list(map(int,input().split()))
    depth = 17
    b = a + [0] * ((1 << depth) - N)
    mst = []
    mstCur = []
    for i in range(1 << depth):
        mstCur.append([b[i]])
    mst.append(mstCur)
    for d in range(1,depth + 1):
        mstCur = []
        for i in range(1 << depth - d):
            mstCurCur = mst[-1][i << 1] + mst[-1][(i << 1) + 1]
            mstCurCur.sort()
            mstCur.append(mstCurCur)
        mst.append(mstCur)
    def query(j, p):
        ans = 0
        depth = 0
        while j != 0:
            if j & 1:
                # Find how many there are on mst[depth][j - 1]
                l = 0
                r = len(mst[depth][j - 1])
                while l < r:
                    k = (l + r) // 2
                    if mst[depth][j - 1][k] > p:
                        r = k
                    else:
                        l = k + 1
                ans += len(mst[depth][j - 1]) - l
            j //= 2
            depth += 1
        return ans
    M = int(input())
    last_ans = 0
    for _ in range(M):
        a,b,c = map(int,input().split())
        a ^= last_ans
        b ^= last_ans
        c ^= last_ans
        last_ans = query(b, c) - query(a - 1, c)
        print(last_ans)


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()


# https://www.acmicpc.net/problem/7469
# 머지소트트리, 세그먼트 트리로도 해보기

import sys
from math import ceil, log2
from bisect import bisect_right


# 머지소트 트리 생성
def infalte_tree(nodes):
    height = ceil(log2(len(nodes)))
    tree = [list() for _ in range(2 << height)]
    end_layer = 1 << height

    for seq, num in enumerate(nodes):
        tree[end_layer + seq] = [num]

    end_layer >>= 1
    while end_layer:
        for i in range(end_layer):
            # 병합정렬
            arr1_idx = arr2_idx = 0

            while arr1_idx < len(tree[(end_layer + i) * 2]) and arr2_idx < len(tree[(end_layer + i) * 2 + 1]):
                if tree[(end_layer + i) * 2][arr1_idx] < tree[(end_layer + i) * 2 + 1][arr2_idx]:
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2][arr1_idx])
                    arr1_idx += 1
                else:
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2 + 1][arr2_idx])
                    arr2_idx += 1

            # 남은 원소 넣어주기
            if arr1_idx != len(tree[(end_layer + i) * 2]):
                for e in range(arr1_idx, len(tree[(end_layer + i) * 2])):
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2][e])

            # 남은 원소 넣어주기
            if arr2_idx != len(tree[(end_layer + i) * 2 + 1]):
                for e in range(arr2_idx, len(tree[(end_layer + i) * 2 + 1])):
                    tree[(end_layer + i)].append(tree[(end_layer + i) * 2 + 1][e])

        end_layer >>= 1

    return tree


# query_start ~ query_end 내 정렬 된 구간 반환
def search(tree, tree_len, query_start, query_end):
    result = []

    # bottom-up 방식
    node_start = tree_len + query_start - 1
    node_end = tree_len + query_end

    while node_start < node_end:
        if node_start & 1:
            result.append(tree[node_start])
            node_start += 1
        if node_end & 1:
            result.append(tree[node_end - 1])
            node_end -= 1

        node_start >>= 1
        node_end >>= 1

    return result


if __name__ == '__main__':
    sys.stdin.readline()    # 노드의 개수, 필요없음
    nodes = [*map(int, sys.stdin.readline().split())]
    n_query = int(sys.stdin.readline())
    tree = infalte_tree(nodes)
    tree_len = 1 << ceil(log2(len(nodes)))
    answer = 0

    for _ in range(n_query):
        i, j, k = map(int, sys.stdin.readline().split())
        src = answer ^ i
        dst = answer ^ j
        target = answer ^ k
        cnt = 0

        for portion in search(tree, tree_len, src, dst):
            cnt += len(portion) - bisect_right(portion, target)

        answer = cnt
        print(answer)

    
import bisect, sys

class MergesortTree():

    def __init__(self, n):
        self.n = 2 ** (n - 1).bit_length()
        self.data = [[] for _ in range(2 * self.n)]

    def set(self, k, v):
        self.data[k + self.n - 1].append(v)

    def build(self):
        for k in reversed(range(self.n - 1)):
            A, B = self.data[k * 2 + 1], self.data[k * 2 + 2]
            i = j = 0
            while i < len(A) and j < len(B):
                if A[i] < B[j]: self.data[k].append(A[i]); i += 1
                else: self.data[k].append(B[j]); j += 1
            while i < len(A): self.data[k].append(A[i]); i += 1
            while j < len(B): self.data[k].append(B[j]); j += 1

    def greater(self, l, r, k):
        L = l + self.n
        R = r + self.n
        ret = 0
        while L < R:
            if R & 1:
                R -= 1
                ret += len(self.data[R - 1]) - bisect.bisect(self.data[R - 1], k)
            if L & 1:
                ret += len(self.data[L - 1]) - bisect.bisect(self.data[L - 1], k)
                L += 1
            L >>= 1
            R >>= 1
        return ret

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = 0

    ST = MergesortTree(N)
    for i, s in enumerate(A):
        ST.set(i, s)
    ST.build()
    for _ in range(Q):
        i, j, k = map(int, input().split())
        i ^= L; j ^= L; k ^= L
        L = ST.greater(i - 1, j, k)
        print(L)
    

from sys import stdin
from bisect import bisect
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
segSize = 1
while segSize < N:
    segSize <<= 1
segTree = [0] * (segSize * 2)
ans = 0

def build():
    global segTree
    for i in range(segSize, segSize * 2):
        try:
            segTree[i] = [A[i - segSize]]
        except:
            segTree[i] = []
    for i in range(segSize-1, 0, -1):
        segTree[i] = sorted(segTree[i<<1] + segTree[i<<1|1])

def query(l, r, k):
    l += segSize
    r += segSize
    res = 0
    while l < r:
        if l&1:
           res += len(segTree[l]) - bisect(segTree[l], k)
           l += 1
        if r&1:
            r -= 1
            res += len(segTree[r]) - bisect(segTree[r], k)
        l >>= 1
        r >>= 1
    return res

build()
for _ in range(M):
    l, r, k = map(int, input().split())
    l ^= ans
    r ^= ans
    k ^= ans
    ans = query(l - 1, r, k)
    print(ans)

import sys
import bisect
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
st = 1
while st<N:
    st<<=1
tree = [[] for _ in range(st*2)]
tmp = st
for i,num in enumerate(list(map(int,input().split())),st):
    tree[i]=[num]
while tmp>1:
    ed = tmp
    tmp = tmp>>1
    for i in range(tmp,ed):
        l,r = 0,0
        left,right = len(tree[i<<1]),len(tree[i<<1|1])
        while l<left or r<right:
            if r==right or l<left and tree[i<<1][l]<tree[i<<1|1][r]:
                tree[i].append(tree[i<<1][l])
                l+=1
            else:
                tree[i].append(tree[i<<1|1][r])
                r+=1
def query(node,ns,ne,s,e,k):
    if ns>e or ne<s: return 0
    if s<=ns and ne<=e:
        return len(tree[node]) - bisect.bisect_right(tree[node],k)
    mid = (ns+ne)>>1
    return query(node<<1,ns,mid,s,e,k)+query(node<<1|1,mid+1,ne,s,e,k)
M = int(input())
ans = 0
for i in range(M):
    a,b,c = map(int,input().split())
    i,j,k = a^ans,b^ans,c^ans
    ans = query(1,1,st,i,j,k)
    output("%d\n"%ans)


import sys
from bisect import bisect
input = sys.stdin.readline
print = sys.stdout.write

def init():
	for i in range(N):
		arr[i+L].append(nums[i])
	for i in range(L-1, 0, -1):
		p = q = 0
		al, bl = len(arr[i*2]), len(arr[i*2+1])
		while p < al and q < bl:
			if arr[i*2][p] <= arr[i*2+1][q]:
				arr[i].append(arr[i*2][p])
				p += 1
			else:
				arr[i].append(arr[i*2+1][q])
				q += 1
		while p < al:
			arr[i].append(arr[i*2][p])
			p += 1
		while q < bl:
			arr[i].append(arr[i*2+1][q])
			q += 1

def query(l, r, k):
	l += L-1; r += L-1
	ret = 0
	len_arr = 1
	while l <= r:
		if l%2 == 1:
			ret += len(arr[l]) - bisect(arr[l], k)
			l += 1
		if r%2 == 0:
			ret += len(arr[r]) - bisect(arr[r], k)
			r -= 1
		l //= 2; r //= 2
	return ret
	
N = int(input())
L = 1 << N.bit_length()
arr = [[] for i in range(L*2)]
nums = list(map(int, input().split()))
Q = int(input())
init()
last_ans = 0
for i in range(Q):
	l, r, k = map(int, input().split())
	l ^= last_ans; r ^= last_ans; k ^= last_ans
	last_ans = query(l, r, k)
	print(str(last_ans)+'\n')