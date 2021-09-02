import sys
input = sys.stdin.readline

var = input().rstrip()
if var[0]=='_':
    print('Error!')
    exit()
var_name = var.split('_')

if len(var_name) > 1:
    answer = ''
    for char in var_name[0]:
        if char.isupper():
            print('Error!')
            exit()
        answer += char
    for var in var_name[1:]:
        if var:
            if var[0].isupper():
                print('Error!')
                exit()
            answer += var[0].upper()
            for char in var[1:]:
                if char.isupper():
                    print('Error!')
                    exit()
                answer += char
        else:
            print('Error!')
            exit()
else:
    answer = ''
    if var[0].isupper():
        print('Error!')
        exit()
    answer += var[0]
    for char in var[1:]:
        if char.isupper():
            answer += '_' + char.lower()
        else:
            answer += char
print(answer)