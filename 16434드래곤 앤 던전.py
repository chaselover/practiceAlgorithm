import sys
input = sys.stdin.readline

def is_clearDungeon(Max_hp, H_atk):
    cur_hp = Max_hp
    for room in dungeon:
        command,atk,health = room[0],room[1],room[2]
        if command==1:
            if health%H_atk==0:
                cur_hp -= ((health//H_atk)-1)*atk
            else:
                cur_hp -= (health//H_atk)*atk
            if cur_hp <=0:
                return False
        else:
            H_atk += atk
            cur_hp = min(Max_hp,cur_hp+health)
    return True


N, H_atk = map(int,input().split())
dungeon = [list(map(int, input().split())) for _ in range(N)]

start = 1
end = int(2e17)
target=0
while start <= end:
    mid = (start+end)//2
    if is_clearDungeon(mid, H_atk):
        end = mid-1
        target = mid
    else:
        start = mid+1

print(target)