arr = list(input())
board = 0
answer = 0
for i in range(len(arr)):
    if arr[i]=='(':
        if arr[i+1]==')':
            answer+=board
            print(f'board:{board}answer:{answer}')
        else:
            board+=1
            print(f'board:{board}answer:{answer}')

    if arr[i]==')':
        if arr[i-1]=='(':
            continue
            print(f'board:{board}answer:{answer}')
        else:
            board-=1
            answer+=1
            print(f'board:{board}answer:{answer}')
print(f'board:{board}answer:{answer}')