from math import sin,acos,pi,sqrt

x0, y0, r0, x1, y1, r1 = map(float, input().split())


def area(x0, y0, r0, x1, y1, r1):
    d = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    rr0 = r0 * r0
    rr1 = r1 * r1
    # 겹치지 않을 때
    if (d > r1 + r0):
        return 0
    # 외접할때
    elif (d <= abs(r0 - r1) and r0 >= r1):
        return pi * rr1
    # 내접할때
    elif (d <= abs(r0 - r1) and r0 < r1):
        # 작은 원의 영역을 출력
        return pi * rr0
    # 겹치는 부분 계산 / 부채꼴 - 삼각형
    else:
        phi = (acos((rr0 + (d * d) - rr1) / (2 * r0 * d))) * 2
        theta = (acos((rr1 + (d * d) - rr0) / (2 * r1 * d))) * 2
        area1 = 0.5 * theta * rr1 - 0.5 * rr1 * sin(theta)
        area2 = 0.5 * phi * rr0 - 0.5 * rr0 * sin(phi)

        return area1 + area2


answer = float(round(1000 * area(x0, y0, r0, x1, y1, r1)) / 1000)
print('%.3f' % answer)