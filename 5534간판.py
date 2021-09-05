import sys
input = sys.stdin.readline

def check(string):
    l = len(string)
    for start_idx in range(l):
        if string[start_idx] == name[0]:
            for end_idx in range(start_idx,l):
                if string[end_idx]==name[-1]:
                    avg_gap = (end_idx-start_idx)//(n-1)
                    cnt = 0
                    while cnt < n:
                        if string[start_idx+avg_gap*cnt]==name[cnt]:
                            cnt += 1
                            continue
                        break
                    else:
                        return 1
    return 0

N = int(input())
name = input().rstrip()
n = len(name)
kanbans = list(input().rstrip() for _ in range(N))
cnt = 0
for kanban in kanbans:
    cnt += check(kanban)
print(cnt)