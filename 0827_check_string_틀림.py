def check(s):
    a_cnt = s.count('a')
    while True:
        if len(s) > 1:
            if s[0]=='b' and s[-1]=='b':
                delete_cnt = 0
                while len(s) > 1 and s[0]=='b' and s[-1]=='b':
                    s = s[1:-1]
                    a_cnt += 1
                if delete_cnt % a_cnt:
                    return False

            elif s[0]=='a' or s[-1]=='a':
                if s[0]=='a':
                    s = s[1:]
                    a_cnt -= 1
                else:
                    s = s[:-1]
                    a_cnt -= 1
        else:
            if s=='a':
                return True
            else:
                return False


def solution(a):
    answer = []
    for string in a:
        answer.append(check(string))
    return answer



print(solution(["bbbbabbbb","abab","abbbbbbbabababbbabbbb","bbaa","bababa","bbbabababbbaa"]))