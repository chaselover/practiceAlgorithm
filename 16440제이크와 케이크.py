import sys
input = sys.stdin.readline

n = int(input())
cakes = input().rstrip()
cnt = 0
for i in range(n//2):
    if cakes[i]=='s':
        cnt += 1
if cnt == n//4:
    print(1)
    print(n//2)
else:
    # 중앙을 기준으로 오른쪽 s면 cnt증가 왼쪽 s면 cnt감소. cnt 맞춰준다(범위를 오른쪽으로 옮기는 과정.)
    # 어차피 자르고 남은 곳도 n//4, n//4이므로 기왕이면 뭉쳐있는곳을 찾는게 나음.
    # 슬라이딩 윈도우.
    for i in range(n//2,n):
        if cakes[i]=='s':
            cnt += 1
        if cakes[i-n//2]=='s':
            cnt -= 1
        if cnt==n//4:
            print(2)
            print(i-n//2+1,i+1)
            break