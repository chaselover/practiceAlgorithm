
 
 
def add_parenthesis(idx, cal_ord):
    global answer
    # 계산 종료
    if idx == N:
        for i, j in enumerate(cal_ord):
            if len(j) == 3:
                cal_ord[i] = str(eval(j))
        result = cal_ord[0]
        for _ in range(1, len(cal_ord), 2):
            result = eval(str(result)+cal_ord[_]+cal_ord[_+1])
 
        if answer < result:
            answer = result
        return
 
    # 연산 기호 넣고
    cal_ord.append(equat[idx])
    # 다음 idx로 넘어감.
    add_parenthesis(idx + 1, cal_ord)
    del cal_ord[-1]
    
    if cal_ord[-1] in symbol and idx + 3 <= N:
        cal_ord.append(equat[idx:idx+3])
        add_parenthesis(idx + 3, cal_ord)
        del cal_ord[-1]
 
N = int(input())
equat = input()
answer = -2 ** 31
 
if N == 1:
    print(max(answer, int(equat)))
    exit()
 
symbol = ["+", "-", "*"]
add_parenthesis(1, [equat[0]])
print(answer)