

N , K= map(int,input().split())
name = list(map(int,input().split()))
concent = []
cnt = 0


for i in range(K):
    if name[i] in concent:
        continue
    else:
        if len(concent)<N:
            concent.append(name[i])
        else:
            max_index = 0
            for j in range(N):
                if concent[j] not in name[i+1:]:
                    change_index = j
                    break
                elif max_index < name[i+1:].index(concent[j]):
                    max_index = name[i+1:].index(concent[j])
                    change_index = j
            concent[j] = name[i]
            cnt +=1

print(cnt)