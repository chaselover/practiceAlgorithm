import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
 
def dist(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)
 
def divide_and_conquer(start, end):
    length = end - start
    if length == 2:
        return dist(location[start], location[start+1])
    elif length == 3:
        return min(dist(location[start], location[start+1]), dist(location[start], location[start+2]), dist(location[start+1], location[start+2]))
    else: # length > 3
        mid = (start + end)//2
        d = min(divide_and_conquer(start, mid), divide_and_conquer(mid, end))
        
        midX = location[mid][0]
        cmp_list = []
        for i in range(start, end):
            if (location[i][0] - midX)**2 <= d:
                cmp_list.append(location[i])
        
        clist_len = len(cmp_list)
        if clist_len >= 2:
            cmp_list.sort(key= lambda x:x[1])
            for i in range(clist_len - 1):
                for j in range(i+1, clist_len):
                    if (cmp_list[i][1] - cmp_list[j][1])**2 > d:
                        break
                    elif cmp_list[i][0] < midX and cmp_list[j][0] < midX:
                        continue
                    elif cmp_list[i][0] >= midX and cmp_list[j][0] >= midX:
                        continue
                    d = min(d, dist(cmp_list[i], cmp_list[j]))
        return d
 
n = int(input())
location = list(set(tuple(map(int, input().split())) for _ in range(n)))
location.sort(key = lambda x: x[0])
if n != len(location):
    print(0)
else:
    print(divide_and_conquer(0, n))