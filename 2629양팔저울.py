import sys
input = sys.stdin.readline

chu_N = int(input())
chu_list = list(map(int,input().split()))

glass_ball_N = int(input())
ball_list = list(map(int,input().split()))

# 추 무게 합이 되는 집합
dp_chu = {i:False for i in range(sum(chu_list)+1)}
# initialize
dp_chu[0] = True

# 추를 더하는 경우만 체크
for chu in chu_list:
    for sum_chu, exist in list(dp_chu.items()):
        if exist:
            if not dp_chu[sum_chu+chu]:
                dp_chu[sum_chu+chu] = True

# 추를 빼는 경우를 체크
# 하나의 추를 더하고 빼는 경우(양쪽에 모두 올려놓는 경우)도 체크하게 되나 결과집합에서는 동일하다.
for chu in chu_list:
    for sum_chu, exist in list(dp_chu.items()):
        if exist:
            if sum_chu-chu >=0 and not dp_chu[sum_chu-chu]:
                dp_chu[sum_chu-chu] = True

# 유리구슬의 한계무게가 추의 한계무게보다 훨씬 크므로 그경우를 배제하면 나머지는 hash table에서 매칭하면 된다.
for ball in ball_list:
    if ball > sum(chu_list):
        print("N", end= " ")
        continue
    if dp_chu[ball]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
else:
    print()