#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
from operator import add

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = int(input())
    AA = SegmentTree([0] * N, func = add)
    q1 = []
    for i in range(N):
        q1.append((A[i], i))
    q2 = []
    ans = [0] * M
    for i in range(M):
        a,b,c = map(int,input().split())
        q2.append((c, a - 1, b, i))
    q1.sort()
    q2.sort()
    while q2:
        while q1 and q1[-1][0] > q2[-1][0]:
            AA[q1[-1][1]] = 1
            q1.pop()
        ans[q2[-1][3]] = AA.query(q2[-1][1], q2[-1][2])
        q2.pop()
    for elem in ans:
        print(elem)

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



# 비재귀 머지 소트 트리
import bisect
import sys
input = sys.stdin.readline

class SortTree:
  def __init__(self, values):
    self.tree = [[x] for x in values]
    self.size = len(self.tree)
    self.tree = [None] * self.size + self.tree
    for i in range(self.size - 1, 0, -1):
      self.tree[i] = sorted(self.tree[i * 2] + self.tree[i * 2 + 1])

  def count_less_than(self, beg: int, end: int, k: int):
    l, r = beg + self.size, end + self.size - 1
    ret = 0
    while l <= r:
      if l % 2:
        ret += bisect.bisect_right(self.tree[l], k)
      if not r % 2:
        ret += bisect.bisect_right(self.tree[r], k)
      l, r = (l + 1) >> 1, (r - 1) >> 1
    return ret

N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
tree = SortTree(A)

ans = [0]*M
for t in range(M):
  i, j, k = [int(x) for x in input().split()]
  ans[t] = (j-i+1) - tree.count_less_than(i-1, j, k)

sys.stdout.write("\n".join(map(str,ans)) + "\n")



# 풀이 3
from sys import stdin
from bisect import bisect
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
start, end = 0, N-1
segSize = 1
while segSize < N:
    segSize <<= 1
segTree = [-1] * (segSize * 2)

def build():
    for i in range(segSize, segSize * 2):
        try:
            segTree[i] = [A[i-segSize]]
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
    left, right, value = map(int, input().split())
    print(query(left - 1, right, value))



# https://www.acmicpc.net/problem/13544
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

    for _ in range(n_query):
        # 문제 조건에 맞게 인덱스 변경
        src, dst, target = map(int, sys.stdin.readline().split())
        cnt = 0

        for portion in search(tree, tree_len, src, dst):
            cnt += len(portion) - bisect_right(portion, target)

        print(cnt)


# 머지트리
import sys
from bisect import bisect
from math import log2, ceil


def merge(arr1, arr2):
    res = []
    i = j = 0
    while True:
        if i == len(arr1):
            return res + arr2[j:]

        if j == len(arr2):
            return res + arr1[i:]

        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1

        else:
            res.append(arr2[j])
            j += 1


n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
height = ceil(log2(n))
tree = [[] for _ in range(2 ** (height + 1))]

for i in range(n):
    tree[2 ** height + i] = [num[i]]

for h in range(height - 1, -1, -1):
    for i in range(2 ** h, 2 ** (h + 1)):
        tree[i] = merge(tree[2 * i], tree[2 * i + 1])


def partial(a, b, k):
    res = 0
    a += 2 ** height - 1
    b += 2 ** height - 1
    while a <= b:
        if a % 2:
            res += len(tree[a]) - bisect(tree[a], k)
            a += 1
        if b % 2 == 0:
            res += len(tree[b]) - bisect(tree[b], k)
            b -= 1
        a //= 2
        b //= 2

    return res


for _ in range(int(sys.stdin.readline())):
    print(partial(*map(int, sys.stdin.readline().split())))



# https://www.acmicpc.net/problem/13537
# segment tree: save sorted list, do binary search

from bisect import bisect_left
from sys import stdin

n = int(stdin.readline().strip())
seq = [[int(i)] for i in stdin.readline().split()]
tree = [[] for _ in range(n)] + seq

# initialize
for i in range(n - 1, -1, -1):
    left = tree[i << 1]
    right = tree[i << 1 | 1]
    # l, r = 0, 0
    # while l < len(left) and r < len(right):
    #     if left[l] < right[r]:
    #         tree[i].append(left[l])
    #         l += 1
    #     elif left[l] > right[r]:
    #         tree[i].append(right[r])
    #         r += 1
    #     else:
    #         tree[i].append(left[l])
    #         tree[i].append(right[r])
    #         l += 1
    #         r += 1
    # if l != len(left):
    #     tree[i] += left[l:]
    # if r != len(right):
    #     tree[i] += right[r:]
    tree[i] = sorted(left + right)


def query(start, end, target):
    start += n - 1
    end += n - 1
    target += 1
    res = 0
    while start < end:
        if start & 1:
            idx = bisect_left(tree[start], target)
            res += len(tree[start]) - idx
            start += 1
        if not end & 1:
            idx = bisect_left(tree[end], target)
            res += len(tree[end]) - idx
            end -= 1
        start >>= 1
        end >>= 1

    if start == end:
        idx = bisect_left(tree[start], target)
        res += len(tree[start]) - idx

    return res


m = int(stdin.readline().strip())
for _ in range(m):
    i, j, k = map(int, stdin.readline().split())
    print(query(i, j, k))




# 머지트리
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
        L = ST.greater(i - 1, j, k)
        print(L)