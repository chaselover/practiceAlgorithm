import random



T = int(input())


def move():
    global i,j
    if direction == 'right':
        j +=1
        if j==C:
            j=0
    if direction == 'left':
        j -=1
        if j==-1:
            j=C-1
    if direction == 'up':
        i -=1
        if i==-1:
            i=R-1
    if direction == 'down':
        i +=1
        if i==R:
            i=0




for test in range(1,T+1):
    memory = 0
    R,C = map(int,input().split())
    game = [list(input()) for _ in range(R)]
    check = []

    i,j=0,0
    direction = 'right'
    

    while 1: 

        if (i,j,direction,memory) in check and game[i][j] != '?':
            answer = 'NO'
            break
        else: 
            check.append((i,j,direction,memory))

        if game[i][j] =='<':
            direction ='left'
            move()

        if game[i][j] =='>':
            direction ='right'
            move()        

        if game[i][j] =='^':
            direction = 'up'
            move()          

        if game[i][j] =='v':
            direction = 'down'
            move()


        if game[i][j] =='_':
            if memory == 0:
                direction ='right'    
            else:
                direction ='left'
            move()

        if game[i][j] =='|':
            if memory == 0:
                direction = 'down'    
            else:
                direction = 'up'
            move()

        if game[i][j] =='?':
            ran_num = random.randint(0,3)
            if ran_num==0:
                direction ='right'    
            elif ran_num==1:
                direction ='left'
            elif ran_num==2:
                direction = 'down'   
            else:
                direction = 'up'
            move()

        if game[i][j].isdigit():
            memory = game[i][j]
            move()

        if game[i][j] =='+':
            memory += 1
            if memory == 16:
                memory = 0
            move()

        if game[i][j] =='-':
            memory = int(memory)
            memory -= 1
            if memory == -1:
                memory = 15    
            move()
        
        if game[i][j] =='.':
            move()

        if game[i][j] == '@':
            answer = 'YES'
            break

        


    print(f"#{test} {answer}")
