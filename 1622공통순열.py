import sys
input = sys.stdin.readline

count = {}
while 1:
    check = ''
    count_cur = {}
    try:
        a = input().rstrip()
        for char in a:
            if char not in count:
                count[char] = 1
            else:
                check += char
    except:
        break
    if check:
        print(check)

