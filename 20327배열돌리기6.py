import sys
input = sys.stdin.readline

def divide_matrix(N,start_x,start_y,end_x,end_y,target_size,rotate_num):
    if N==target_size:
        rotate_matrix(N,start_x,start_y,end_x,end_y,target_size,rotate_num)
    half = 1<<(N-1)
    divide_matrix(N-1,start_x,start_y,half,half,target_size,rotate_num)
    divide_matrix(N-1,start_x,half,half,end_y,target_size,rotate_num)
    divide_matrix(N-1,half,start_y,end_x,half,target_size,rotate_num)
    divide_matrix(N-1,half,half,end_x,end_y,target_size,rotate_num)

def rotate_matrix(N,start_x,start_y,end_x,end_y,target_size,rotate_num):
    if rotate_num==1:
        pass


N,R = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(1<<N)]
for _ in range(R):
    target_unit, rotate_num = map(int,input().split())
    divide_matrix(N,0,0,1<<N,1<<N,target_unit,rotate_num)