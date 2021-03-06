def make_set(s):
    a = set()
    for i in range(len(s) - 1):
        now = s[i:i+2]
        if now.isalpha():
            while now in a:
                now += '1'
            a.add(now)
    return a

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    a = make_set(str1)
    b = make_set(str2)
    if not a | b:
        return 65536
    return len(a & b) * 65536 // len(a | b)