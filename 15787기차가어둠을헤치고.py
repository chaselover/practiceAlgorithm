import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trains = [[0]*20 for _ in range(N)]

for _ in range(M):
    command = input().split()
    train_num = int(command[1])-1
    if command[0] == '1':
        trains[train_num][int(command[2])-1] = 1
    elif command[0] == '2':
        trains[train_num][int(command[2])-1] = 0
    elif command[0] == '3':
        for i in range(19,0,-1):
            trains[train_num][i] = trains[train_num][i-1]
        trains[train_num][0] = 0
    elif command[0] == '4':
        for i in range(19):
            trains[train_num][i] = trains[train_num][i+1]
        trains[train_num][19] = 0

train_list = [True]*N
for i in range(N):
    if not train_list[i]:
        continue
    for j in range(i+1,N):
        if train_list[j] and trains[i]==trains[j]:
            train_list[j] = False

print(sum(train_list))
