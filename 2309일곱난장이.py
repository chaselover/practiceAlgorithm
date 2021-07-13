import sys
input = sys.stdin.readline

# 키의 합이 100 9명 중 7명의

dwarf = [int(input()) for _ in range(9)]

for i in range(1,9):
    for j in range(i):
        if sum(dwarf)-(dwarf[i]+dwarf[j])==100:
            del dwarf[i]
            del dwarf[j]
            dwarf.sort()
            for k in range(7):
                print(dwarf[k])
            exit()

