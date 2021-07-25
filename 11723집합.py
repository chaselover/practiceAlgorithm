import sys
input = sys.stdin.readline
m = int(input())
S = set()

for _ in range(m):
    commands = input().strip().split()
    
    # split()을 통해 띄어씌기가 있으면 튜플인 commands
    # 없으면 그냥 commands
    if len(commands) == 1:
        if commands[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    # set은 add remove discard(discard는 없는거 없애려해도 오류아냄.)
    else:
        command, num = commands[0], commands[1]
        num = int(num)

        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check":
            print(1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)