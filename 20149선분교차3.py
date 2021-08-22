import sys

INF = float('inf')
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())


def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0


def findA(x1, y1, x2, y2):
    if x1 == x2:
        return INF
    else:
        return (y2 - y1) / (x2 - x1)


def findB(x1, y1, a):
    return y1 - a * x1


def findFunc(x1, y1, x2, y2):
    a = findA(x1, y1, x2, y2)
    if a == INF:
        if y1 == y2:
            return x1, y1, True
        return x1, INF, True
    b = findB(x1, y1, a)
    return a, b, False


def findPoint(x1, y1, x2, y2, x3, y3, x4, y4):
    a1, b1, flag1 = findFunc(x1, y1, x2, y2)
    a2, b2, flag2 = findFunc(x3, y3, x4, y4)
    if flag1:
        if b1 == INF:
            return a1, a2 * a1 + b2
        return x1, y1
    if flag2:
        if b2 == INF:
            return a2, a1 * a2 + b1
        return x3, y3
    else:
        if a2 != a1:
            return (b1 - b2) / (a2 - a1), (b1 * a2 - b2 * a1) / (a2 - a1)
        else:
            if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                if min(x1, x2) == max(x3, x4):
                    return min(x1, x2), min(x1, x2) * a1 + b1
                if max(x1, x2) == min(x3, x4):
                    return max(x1, x2), max(x1, x2) * a1 + b1
                return INF, INF


ans = 0
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        ans = 1
elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    ans = 1
print(ans)
if ans == 1:
    xans, yans = findPoint(x1, y1, x2, y2, x3, y3, x4, y4)
    if xans != INF and yans != INF:
        if xans % 1 == 0:
            xans = round(xans)
        if yans % 1 == 0:
            yans = round(yans)
        print(xans, yans)