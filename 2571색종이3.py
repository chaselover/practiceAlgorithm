import sys
input = sys.stdin.readline

def find_rectangle(x,y):

    max_size = 100
    for i in range(100):
        if x+i >100:
            break
        for j in range(100):
            if y + j > 100:
                break
            max_size = max(max_size,calculate_area(x,y,x+i,y+j))
    return max_size

def calculate_area(x,y,h,w):
    cnt = 0
    for i in range(x,h+1):
        for j in  range(y,w+1):
            if not paper[i][j]:
                return 0
            else:
                cnt += 1
    return cnt
        


n = int(input())
paper = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

max_size = 100
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            max_size = max(max_size,find_rectangle(i,j))
print(max_size)




# 다른 답.
import sys
input = sys.stdin.readline


paper = [[0]*102 for _ in range(100)]
for i in range(int(input())):
    x, y = map(int,input().split())
    for i in range(x+1,x+11):
        for j in range(y,y+10): 
            paper[j][i]=1

# 0행을 기준으로 높이값을 저장.(1이 이어지는 길이)
for i in range(1,100):
    for j in range(1,102):
        if paper[i][j]: 
            paper[i][j]=paper[i-1][j]+1

max_size = 0
# 행 순회
for row in range(100):
    paper_row = paper[row]
    # S는 계산하지 않은 열을 넣을 이전 열 idx stack 최초 값 0은 0열의 높이값은 모두 0이기 때문에 기준으로 삼기 위해.
    pre_idx_stack = [0]
    # 열 순회
    for cur_col in range(1,102):
        # S는 마지막으로 살펴본 열의 idx 현재 살펴보는열의 높이가 이전 열의 높이보다 작으면 같아질떄까지 s빼면서 직사각형 비교해줌.
        # 높이가 작아진다는 말은 곧 위에 빈칸이 있다는 뜻으로 빈칸이 반영 되기 이전에 높은 값에 대해 최대높이를 갱신시킨 후 넘어가겠다는 뜻.
        while pre_idx_stack and paper_row[pre_idx_stack[-1]] > paper_row[cur_col]:
            h = paper_row[pre_idx_stack[-1]]
            pre_idx_stack.pop()
            # cur_col-1는 현재 idx 바로 이전값 pre_idx_stack[-1]은 h높이를 가지는idx 
            max_size = max(max_size, (cur_col-pre_idx_stack[-1]-1)*h)
        pre_idx_stack.append(cur_col)
print(max_size)