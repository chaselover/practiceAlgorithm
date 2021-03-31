#N개의 보물상자, 각각 다른 키를 사용, 한번쓰면 다시 못씀.
#각 보물상자->보물, 다른 보물상자의 키들이 하나 이상 들어있다.
#어떤 키가 들어있는지는 열기 전에 이미 알고있음.
#나는 이미 K개의 키를 가지고있음.

#=> 모든상자를 열수있는가? 열수있다면 사전 순 최소인 방법을 출력하라.


"""
출력
열수없으면 IMPOSSIBLE
있으면 상자 여는 순서 N개 정수. 여러개면 사전순 최소인 순서를 출력
"""

#결국 DFS구현(가다가 아니면 돌아옴)
#인덱스를 상자넘버(키종류)
#그래프 구현
#dfs 구현
#입출력


    

def DFS_find_treasure(v, discovered=[]):
    
    for w in boxes[v]:
        if not w in discovered:
            discovered.append(w)
            discovered = DFS_find_treasure(w,discovered)
    return discovered

T = int(input())

for test_case in range(T):
    K, N = map(int,input().split())
    boxes = {}
    boxes[0] = list(map(int,input().split()))
    for Box_Num in range(N):
        Ti_Ki_TiNo = list(map(int,input().split()))
        Ti = Ti_Ki_TiNo[0]
        Ki = Ti_Ki_TiNo[1]
        TiNo = [0]*Ki
        for i in range(2,Ki+2):
            TiNo[i-2] = Ti_Ki_TiNo[i]
            boxes[Ti] = TiNo
    
    if N != len(DFS_find_treasure(0)):
        print("IMPOSSIBLE")
    else:
        print("#{} {}".format(test_case+1,DFS_find_treasure(0)))