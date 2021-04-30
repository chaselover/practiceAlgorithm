import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
arr2 = []
max = 0
answer = ''
while arr:
    a = arr.pop()
    if arr2:
        for s in arr2[::-1]:
            if a<s:
                answer = str(s) + ' ' + answer
                arr2.append(a)
                break
            if a>max:
                answer = '-1 ' + answer
                arr2.append(a)
                max = a
                break
    else:
        answer = '-1 ' + answer
        arr2.append(a)
        max = a

print(answer)


