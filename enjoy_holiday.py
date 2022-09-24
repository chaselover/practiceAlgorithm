import heapq


N = int(input())
cards =[]
times = 0

for _ in range(N):
    heapq.heappush(cards,int(input())


if(N==1)
    print(0)
    else:
    while len(cards) > 1:
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        times += card1 + card2
        heapq.heappush(cards,card1+card2)


print(times)

