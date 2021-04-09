# N개의도시 일직선
#왼 -> 오
# 도시간 거리 가중치.km단위
# 기름통 무제한 km당 1리터
#도시당 주유소 1개 리터당 가격 다름
# 오른쪽 까지 가는 최소비용.
#
#
#
#정점N개 간선 N-1개

N = int(input())
distance = list(map(int,input().split()))
pricePerKm = list(map(int,input().split()))
mincost = pricePerKm[0]
totalCost = 0


for i in range(N-1):
    if mincost>=pricePerKm[i]:
        mincost = pricePerKm[i]
        totalCost += mincost*distance[i]
    else:
        totalCost +=mincost*distance[i]

print(totalCost)