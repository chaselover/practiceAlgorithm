import sys
input = sys.stdin.readline

def draw(n,idx):
    if n==1:
        stars[idx][idx] = '*'
        return ;
    l = 4*n-3

    for i in range(idx,l+idx):
        stars[idx][i]='*'
        stars[idx+l-1][i]='*'

        stars[i][idx]='*'
        stars[i][idx+l-1]='*'

    return draw(n-1,idx+2)

n = int(input()) # n을 입력받는다.
lens = 4*n -3

stars = [[' ']*lens for _ in range(lens) ]

draw(n,0)

for i in range(lens):
    for j in range(lens):
        print(stars[i][j],end="")
    print()


# 풀이 2
num = int(input())
print('*'*(1+(num-1)*4))
for i in range(1, 2*num-1):
    if i % 2:
        print('* '*((i+1)//2) + ' '*(1+(num-1)*4-(i+1)//2*4) + ' *'*((i+1)//2))
    else:
        print('* '*((i+1)//2) + '*'*(1+(num-1)*4-(i+1)//2*4) + ' *'*((i+1)//2))
for i in range(2*num-3, 0, -1):
    if i % 2:
        print('* '*((i+1)//2) + ' '*(1+(num-1)*4-(i+1)//2*4) + ' *'*((i+1)//2))
    else:
        print('* '*((i+1)//2) + '*'*(1+(num-1)*4-(i+1)//2*4) + ' *'*((i+1)//2))
if num != 1:
    print('*'*(1+(num-1)*4))