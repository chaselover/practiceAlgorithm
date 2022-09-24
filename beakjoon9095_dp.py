import sys

T = int(sys.stdin.readline())

N,W = map(int,sys.stdin.readline().split())

circle = [list(map(int,sys.stdin.readline().split()))for _ in range(2)]

check = [[0]*8 for _ in range(2)]
cnt = 0

for j in range(2):
    for i in range(8):
        if check[i][j] ==0:
            if circle[i][j] < W:
                if circle[i][j]+circle[(i-1)%8][j] <=100 and check[(i-1)%8][j] ==0:
                    check[i][j], check[(i-1)%8][j] = 1,1
                    cnt +=1
                elif circle[i][j]+circle[(i+1)%8][j] <=100 and check[(i+1)%8][j] ==0:
                    check[i][j], check[(i+1)%8][j] = 1,1
                    cnt +=1
                elif circle[i][j]+circle[i][(j-1)%2] <=100 and check[i][(j-1)%2] ==0:
                    check[i][j], check[i][(j-1)%2] = 1,1
                    cnt +=1   
                elif circle[i][j]+circle[i][(j+1)%2] <=100 and check[i][(j+1)%2] ==0:
                    check[i][j], check[i][(j+1)%2] = 1,1
                    cnt +=1
                else:
                    check[i][j]=1
                    cnt +=1

print(cnt)