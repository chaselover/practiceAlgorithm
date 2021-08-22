import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
 
def dist(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)
 
def divide_and_conquer(start, end):
    length = end - start
    # 거리 구하기 쉬운 2~3개 남을 때까지 분할해서 정복한다.
    if length == 2:
        return dist(location[start], location[start+1])
    elif length == 3:
        return min(dist(location[start], location[start+1]), dist(location[start], location[start+2]), dist(location[start+1], location[start+2]))
    else: # length > 3
        #  중앙을 기준으로 분할
        mid = (start + end)//2
        # 분할 결과중 최솟값만 가져옴.
        d = min(divide_and_conquer(start, mid), divide_and_conquer(mid, end))
        
        # x의 중앙값.(중앙값 좌표의 x)
        midX = location[mid][0]
        cmp_list = []
        # 그 좌표로부터 x 거리 제곱이 d 보다 작으면 후보군에 삽입.
        for i in range(start, end):
            if (location[i][0] - midX)**2 <= d:
                cmp_list.append(location[i])
        
        clist_len = len(cmp_list)
        if clist_len >= 2:
            # y 에 대해 정렬
            cmp_list.sort(key= lambda x:x[1])
            # 모든 정점 조합에 대해 거리 검사.
            for i in range(clist_len - 1):
                for j in range(i+1, clist_len):
                    # y좌표 차이의 제곱이 d보다 작고 x좌표가 중앙값에 걸쳐있는 애들만 d에 최솟값 거리 비교를 해줌. 중앙값에 안걸쳐있으면 다 거름.
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
# 1. x에 대해 정렬.
location.sort(key = lambda x: x[0])
if n != len(location):
    print(0)
else:
    print(divide_and_conquer(0, n))