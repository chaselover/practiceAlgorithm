def solution(n, left, right):
    arr = []
    start_x, start_y, end_x = left // n, left % n, right // n
    for i in range(start_x, end_x + 1):
        arr += [i + 1] * (i + 1) + [j for j in range(i + 2, n + 1)]
    return arr[start_y: start_y + right - left + 1]

