import sys
###인풋
T = int(sys.stdin.readline())
cntA = 0
cntB = 0
cntC = 0

if T%10 !=0:
    print("-1")
else:
    cntA += T//300
    T = T%300
    cntB += T//60
    T = T%60
    cntC += T//10
    print(f'{cntA} {cntB} {cntC}')