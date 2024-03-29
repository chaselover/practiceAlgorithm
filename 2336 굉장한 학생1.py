"""Solution code for "BOJ 2336. 굉장한 학생".

- Problem link: https://www.acmicpc.net/problem/2336
- Solution link: http://www.teferi.net/ps/problems/boj/2336

(This code was generated by Import Inliner v0.1)
"""

import operator
import sys
from typing import Callable, Iterable, TypeVar

INF = float('inf')
T = TypeVar('T')


# >>>[BEGIN] teflib.segmenttree.SegmentTree [v1.1] (Copied from teflib/segmenttree.py)<<<
class SegmentTree:
    """Non-recursive segment tree supporting point update and range query."""

    def __init__(self,
                 values: Iterable[T],
                 merge: Callable[[T, T], T] = operator.add):
        l = list(values)
        self._size = len(l)
        self._tree = [0] * self._size + l
        self._merge = merge
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = merge(self._tree[i * 2], self._tree[i * 2 + 1])

    def update(self, pos: int, value: T):
        i = pos + self._size
        while i:
            self._tree[i] = self._merge(self._tree[i], value)
            i >>= 1

    def query(self, beg: int, end: int) -> T:
        ret = self._tree[beg + self._size]
        l, r = beg + self._size + 1, end + self._size - 1
        while l <= r:
            if l % 2:
                ret = self._merge(self._tree[l], ret)
            if not r % 2:
                ret = self._merge(self._tree[r], ret)
            l, r = (l + 1) >> 1, (r - 1) >> 1
        return ret
# >>>[END] teflib.segmenttree.SegmentTree [v1.1]<<<


def main():
    N = int(sys.stdin.readline())
    student_to_rank = [0] * (N + 1)
    for rank, student in enumerate(sys.stdin.readline().split()):
        student_to_rank[int(student)] = rank
    ranks = [[0, 0] for _ in range(N)]
    for test_num in range(2):
        for rank, student in enumerate(sys.stdin.readline().split()):
            ranks[student_to_rank[int(student)]][test_num] = rank

    segtree = SegmentTree([INF] * N, min)
    answer = 0
    for rank2, rank3 in ranks:
        if segtree.query(0, rank2) > rank3:
            answer += 1
        segtree.update(rank2, rank3)

    print(answer)


if __name__ == '__main__':
    main()