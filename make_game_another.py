direction = '<>^v|_'
memory = '0123456789'
operator = '+-'
ee = 0
 
def dfs(mem, rDir, cDir, dirct):
    global ans
    global visited
    global ee
     
    pattern = hyuk[rDir][cDir]
    tmp = mem+str(rDir)+str(cDir)+dirct
    if ee == 1:
        return
    #print("##",pattern,"%%",[mem,rDir, cDir, dirct])
    if tmp in visited:
        #ee = 1
        #print('duplic')
        return
    else:
        visited.append(tmp)
     
    if pattern == '@':
        ee = 1
        ans = 'YES'
        return
    #print(pattern, "!!", visited, "@@", [mem, rDir, cDir, dirct])
    if pattern in operator:
        if pattern == '+':
            mem = str((int(mem)+1)%16)
        else:
            mem = str((int(mem)-1)%16)
    if pattern in memory:
        mem = pattern
     
     
    if pattern == '?':
        if hyuk[(rDir+1)%row][cDir] == '@' or hyuk[(rDir-1)%row][cDir] == '@' or hyuk[rDir][(cDir+1)%col] == '@' or hyuk[rDir][(cDir-1)%col] == '@':
            ans = 'YES'
            ee = 1
            return
        else:
            for i in range(4):
                if i == 0:
                    #rDir = (rDir+1)%row
                    dirct = 'down'
                    dfs(mem, (rDir+1)%row, cDir, dirct)
                if i == 1:
                    #rDir = (rDir-1)%row
                    dirct = 'up'
                    dfs(mem, (rDir-1)%row, cDir, dirct)
                if i == 2:
                    #col = (cDir+1)%col
                    dirct = 'right'
                    dfs(mem, rDir, (cDir+1)%col, dirct)
                if i == 3:
                    #col = (cDir-1)%col
                    dirct = 'left'
                    dfs(mem, rDir, (cDir-1)%col, dirct)
                #print("?",[r, c, dirct])
                #dfs(mem, r, c, dirct)
                 
    else:
        if pattern in direction:
            if pattern == '>':
                dirct = 'right'
            elif pattern == '<':
                dirct = 'left'
            elif pattern == '^':
                dirct = 'up'
            elif pattern == 'v':
                dirct = 'down'
            elif pattern == '|':
                if mem == '0':
                    dirct = 'down'
                else:
                    dirct = 'up'
            elif pattern == '_':
                if mem == '0':
                    dirct = 'right'
                else:
                    dirct = 'left'
             
        if dirct == 'right':
            cDir = (cDir+1)%col
        elif dirct == 'left':
            cDir = (cDir-1)%col
        elif dirct == 'up':
            rDir = (rDir-1)%row
        elif dirct == 'down':
            rDir = (rDir+1)%row
         
 
        dfs(mem, rDir, cDir, dirct)
     
 
numtest = int(input())
for testCnt in range(numtest):
    row, col = input().split()
    row = int(row)
    col = int(col)
    flag = 0
    hyuk = [['']*col for i in range(row)]
    #visited = [[['-1',-1,-1,'X']]*col for i in range(row)]
    visited = []
    ans = 'NO'
    ee = 0
    
    '''
    hyuk = [a for a in input().split()]
    for item in hyuk:
        if '@' in item:
            flag = 1
    '''
    for rowcnt in range(row):
        hyuk[rowcnt] = input()
        if '@' in hyuk[rowcnt]:
            flag = 1
     
    for i in range(row):
        for j in range(col):
            if hyuk[i][j] == '@':
                if hyuk[(i-1)%row][j] != 'v' and hyuk[(i-1)%row][j] in direction and hyuk[(i+1)%row][j] != '^' and hyuk[(i+1)%row][j] in direction and hyuk[i][(j-1)%col] != '>' and hyuk[i][(j-1)%col] in direction and hyuk[i][(j+1)%col] != '<' and hyuk[i][(j+1)%col] in direction:
                    flag = 0
                    break
                 
                 
    #visited[0][0] = ['0',0,0,'right']
    if flag == 1:
        dfs('0', 0, 0, 'right')
         
    print("#%d %s" % (testCnt+1, ans))