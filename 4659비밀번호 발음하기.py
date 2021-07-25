import sys
input = sys.stdin.readline



# 모음3개, 자음3개 연속 x
# 같은글자 연속 두번 x ee,oo는 허용

while 1:
    good_pwd = input().strip()
    if good_pwd == 'end':
        break
    N = len(good_pwd)
    mom_chr = ['a','e','i','o','u']
    mom_cnt = 0
    child_cnt = 0
    answer = False

    for i in range(N):
        if good_pwd[i] in mom_chr:
            mom_cnt +=1
            answer = True
            child_cnt = 0
        else:
            child_cnt +=1
            mom_cnt = 0

        if mom_cnt == 3 or child_cnt ==3:
            answer = False
            break

        if i>0 and good_pwd[i] ==good_pwd[i-1]:
            if good_pwd[i]=='e' or good_pwd[i]=='o':
                continue
            else:
                answer=False
                break

    if answer:
        print(f'<{good_pwd}> is acceptable.')
    else:
        print(f'<{good_pwd}> is not acceptable.')