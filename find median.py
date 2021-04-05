
T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    points = list(map(int,input().split()))
    for i in range(N):
        for x in points:
            points.append(x + points[i])

    grades = set(points)
    answer = len(grades)
    print("#{} {}".format(test_case, answer))