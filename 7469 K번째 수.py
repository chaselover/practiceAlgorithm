import bisect
import operator
import sys


class MergeSortTreeForKthElem:
    def __init__(self, values):
        l = [[i] for i, value
             in sorted(enumerate(values), key=operator.itemgetter(1))]
        self._values = values
        self._size = 1 << (len(l) - 1).bit_length()
        self._tree = ([[] for _ in range(self._size)]
                      + l + [[]] * (self._size - len(l)))
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = self._tree[i * 2] + self._tree[i * 2 + 1]
            self._tree[i].sort()

    def kth(self, beg: int, end: int, k: int) -> int:
        i = 1
        while i < self._size:
            i += i
            node = self._tree[i]
            t = bisect.bisect_left(node, end) - bisect.bisect_left(node, beg)
            if t < k:
                k -= t
                i += 1
        return self._values[self._tree[i][0]]


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    nums = [int(x) for x in sys.stdin.readline().split()]
    mst = MergeSortTreeForKthElem(nums)
    for _ in range(m):
        i, j, k = [int(x) for x in sys.stdin.readline().split()]
        print(mst.kth(i - 1, j, k))


if __name__ == '__main__':
    main()
