import sys

n = int(sys.stdin.readline())
wine = []
drink = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))


drink.append(wine[0])
if n>1:
    drink.append(wine[0]+wine[1])
if n>2:
    drink.append(max(wine[0]+wine[2],wine[1]+wine[2]))
if n>3:
    for i in range(3,n):
        drink.append(max(drink[i-2]+wine[i],drink[i-3]+wine[i-1]+wine[i],drink[i-1]))

print(drink[n-1])

# 출발지점, 도착지점이 정해지지 않으면 이전까지 모든 값중 max값을 찾으면됨.
# 그리고 두칸띄워도됨.