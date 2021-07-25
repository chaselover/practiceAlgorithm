import sys
input = sys.stdin.readline

# 1. 스도쿠에 빈 공간(0)이 있는지 확인한다. 
# 2. 빈 공간이 없으면 스도쿠가 완성됐으므로 종료한다.
# 3. 빈 공간이 있으면 빈 공간(col, row)이 어딘지 말한다.
# 4. 빈 공간에 어떤 값(1~9)이 들어갈 수 있는지 탐색한다.
#  - 찾았다면 스도쿠에 채워넣는다.
#  - 채워넣을 수 있는 게 없다면 백 트래킹 한다.

def cal(x, y):
    return (x//3)*3 + (y//3)

def solve_sudoku(n):
    # 81칸 전부 캄색하고 배열 출력.
    if n == 81:
        for i in sudoku:
            print(''.join(map(str, i)))
        return True

    x,y = divmod(n,9)
    # 있다면 다음칸으로 넘어가고
    if sudoku[x][y]: 
        return solve_sudoku(n+1)
    else:
        # 1~10숫자중에 뭘 넣을까 찾아본다. 3가지 항목 체크하고 숫자기입. 안되면 백트래킹
        for i in range(1, 10):
            if not check_col[x][i] and not check_row[y][i] and not check_square[cal(x,y)][i]:
                check_col[x][i] = check_row[y][i] = check_square[cal(x,y)][i] = True
                sudoku[x][y] = i
                # True값 반환오면 바로 True값 반환해서 빠르게 돌아가게 한다.
                if solve_sudoku(n+1): 
                    return True
                # 아니면 다시 숫자 뺀다.
                check_col[x][i] = check_row[y][i] = check_square[cal(x,y)][i] = False
                sudoku[x][y] = 0
    # 1~10 다 안되면 일단 뺀다.
    return False


sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
# 각 9개의 행, 열, 사각형에 1~9까지의 숫자가 있냐 없냐 check
check_col = [[False]*10 for _ in range(9)] #행
check_row = [[False]*10 for _ in range(9)] #열
check_square = [[False]*10 for _ in range(9)] #사각형
for i in range(9):
    for j in range(9):
        if sudoku[i][j]:
            check_col[i][sudoku[i][j]] = True
            check_row[j][sudoku[i][j]] = True
            check_square[cal(i, j)][sudoku[i][j]] = True

solve_sudoku(0)