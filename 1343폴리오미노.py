import sys
input = sys.stdin.readline

s = input().rstrip() + '.'
answer=''
cnt=0
for chr in s:
    if chr=='X':
        cnt+=1
        if cnt==4:
            answer+='AAAA'
            cnt=0
    else:
        if cnt==2:
            answer+='BB.'
            cnt=0
        elif cnt==0:
            answer+='.'
        else:
            print(-1)
            exit()
print(answer[:-1])