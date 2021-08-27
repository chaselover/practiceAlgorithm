def check(s):
    
    while not s=='a':
        
        if s[0]=='b' and s[-1]=='b':
            a_cnt = 0
            while s and s[0]=='b' and s[-1]=='b':
                s = s[1:-1]
                a_cnt += 1
            if not s.count('a')==a_cnt:
                return False

        elif len(s) != 1 and (s[0]=='a' or s[-1]=='a'):
            if s[0]=='a':
                s = s[1:]
            else:
                s = s[:-1]
    return True



def solution(a):
    answer = []
    for string in a:
        answer.append(check(string))
    return answer



print(solution(["a","abab","abbbbbbbabababbbabbbb","bbaa","bababa","bbbabababbbaa"]))