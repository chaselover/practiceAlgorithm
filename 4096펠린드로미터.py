case = input()

while(int(case)):
    length = len(case)
    num = int(case)
    answer = 0
    while(1):
        if case == case[::-1]:
            break
        num = num + 1
        answer = answer + 1
        case = str(num).zfill(length)
    print(answer)
    case = input()
    if case == '0':
        break
