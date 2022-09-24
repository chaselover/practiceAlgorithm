



sudoku = [list(map(int,input().split())) for _ in range(9)]
check = [[0]*9 for _ in range(9)]
sum_check_square = 0
sum_square = 0
cnt = 0
check_cnt=0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] ==0:
            check[i][j] =1
            cnt +=1

while cnt != check_cnt:
    for i in range(9):
        for j in range(9):
            if check[i][j]==1:
                if sum(check[i])==1:
                    sudoku[i][j] = 45-sum(sudoku[i])
                    check[i][j] =0
                    check_cnt +=1
                if sum([check[n][j] for n in range(9)]) ==1:
                    sudoku[i][j] = 45- sum([sudoku[m][j] for m in range(9)])
                    check[i][j] =0
                    check_cnt +=1
                for p in range((i//3)*3,(i//3)*3+3):
                    for q in range((j//3)*3,(j//3)*3+3):
                        sum_check_square +=check[p][q]
                        sum_square +=sudoku[p][q]
                if sum_check_square ==1:
                    sudoku[i][j] = 45-sum_square
                    check[i][j] = 0
                    check_cnt +=1

for row in sudoku:
    print(*row)
