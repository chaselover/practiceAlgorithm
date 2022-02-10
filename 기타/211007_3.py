def solution(n, m, x, y, queries):
    # 도착점부터 거꾸로 이행을 한다. left, right, up, down의 범위를 조정해감.(x1, y1), (x2, y2)
    # 도착점과 command set을 가지고 시작할 수 있는 범위를 돌려주는 함수.
    # 연속 부분 이차원 배열의 연산결과는 연속 부분 이차원 배열이 나옴.
    # 그 여백의 넓이가 문제의 답.

    # 음수구간 고려해야함.
    
    # max_x, min_x ,y 이분탐색으로 구해서 범위를 구한다. -> 얘는 따로 x, y 따로해서 구할 수 있음.(축마다 따로)
    answer = -1
    return answer




print(solution(2, 2, 0, 0))