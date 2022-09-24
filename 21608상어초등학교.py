import sys
from collections import defaultdict
input = sys.stdin.readline

def check(j,k):
    near_list = []
    empty = 0
    for i in range(4):
        if j+dx[i] >=0 and j+dx[i] < n and k+dy[i] >=0 and k+dy[i] < n:
            if table[j+dx[i]][k+dy[i]]:
                near_list.append(table[j+dx[i]][k+dy[i]])
            else:
                empty += 1

    return near_list,empty

def find_seat(l):
    l = sorted(l, key=lambda x:(x[0], x[1], x[2], x[3]))
    cnt,emp,x,y = l[0]
    return x,y

n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
student = defaultdict(list)

for _ in range(n*n):
    temp = list(map(int, input().split()))
    student[temp[0]] = temp[1:]

table = [[False] * n for _ in range(n)]

for i in student.keys():
    l = []
    temp =[]
    cnt = 0
    like_friend = 0 # i가 앉을수있는 위치에서 좋아하는 친구들의 수
    for j in range(n):
        for k in range(n):
            if table[j][k]: # 누가 앉아있으면 건너뛰고
                continue
            #i학생이 j,k에 앉았을때 인접한 친구들과 인접한 빈칸의 수
            near_list, emp = check(j,k)
            for like in student[i]:
                if like in near_list:
                    cnt += 1
            temp.append(-cnt)
            temp.append(-emp)
            temp.append(j)
            temp.append(k)
            l.append(temp)
            temp = []
            cnt = 0

    #print(l) # l- 친구리스트와 빈칸, 해당 자리
    x,y = find_seat(l)
    table[x][y] = i

answer = 0
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
for i in range(n):
    for j in range(n):
        count = 0
        friend_list = check(i,j)[0]
        for f in friend_list:
            if f in student[table[i][j]]:
                count += 1
        answer += score[count]

print(answer)