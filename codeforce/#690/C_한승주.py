import sys
input = sys.stdin.readline
from bisect import bisect_right 


for test in range(int(input())):
    a, b, k = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    if k == 1:
        print(0)
        continue
    sets = []
    for i in range(k):
        num_a, num_b = arr_a[i], arr_b[i]
        for each_set in sets:
            if ('a', num_a) not in each_set and ('b', num_b) not in each_set:
                each_set.add(('a', num_a))
                each_set.add(('b', num_b))
        sets.append({('a', num_a), ('b', num_b)})
    print(sets)
    cnt = 0
    for each_set in sets:
        pairs = len(each_set) // 2
        cnt += pairs * (pairs - 1) // 2
    print(cnt)