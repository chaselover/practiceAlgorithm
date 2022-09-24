from collections import Counter

def rc():
    max_len = 0
    len_s = len(s)
    for j in range(len_s):
        a = [i for i in s[j] if i != 0]
        a = Counter(a).most_common()
        # 갯수기준, 수기준 정렬
        a.sort(key = lambda x : (x[1], x[0]))
        # 그 행 비우고 새 원소로 넣어줌.
        s[j] = []
        for fi, se in a:
            s[j].append(fi)
            s[j].append(se)
        len_a = len(a)
        # 최대 길이 체크(가장 큰 열 기준 모든 열의 크기 변함)
        if max_len < len_a * 2: 
            max_len = len_a * 2
    # 빈칸에 0 채워줌.
    for j in range(len_s):
        for _ in range(max_len - len(s[j])):
            s[j].append(0)
        # 100개 넘어가면 그냥 자름.
        s[j] = s[j][:100]


r, c, k = map(int, input().split())
s = [list(map(int, input().split())) for i in range(3)]
for i in range(101):
    try:
        if s[r - 1][c - 1] == k:
            print(i)
            break
    except: 
        pass
    if len(s) < len(s[0]):
        s = list(zip(*s))
        rc()
        s = list(zip(*s))
    else:
        rc()
else:
    print(-1)