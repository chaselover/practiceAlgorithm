import sys
input = sys.stdin.readline

# 
def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        # 일치하지 않으면 그 이전 위치에서의 반복값으로 인덱스를 되돌린다.
        # 즉 비교군 j의 인덱스를 이전에 일치했던 곳으로 되돌려 pattern매칭을 해본다. 또 틀리면 그전으로 그전으로. 해서 다시 번호를 적어나간다.
        # 결국 일치하는게 없다면 j는 0까지 되돌아간다.
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        # 일치하면 일치한 곳에 +1해주면서 몇개가 반복되나 체크.
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

def KMP(s, pattern):
    getPI(pattern)
    # 배열이 완성되었다면 s배열과 pattern배열을 비교해야한다. 
    # s와 pattern이 일치한다면 j를 계속 늘리며 비교해 j의 크기가 pattern배열만큼 커지면 True를 반환.
    # 중간에 불일치가 일어난다면 j의 위치를 또 그 이전 불일치가 일어났던 곳으로 한칸씩 당기며 s와 비교한다.
    # 없다면 또 j는 0으로 돌아간다.
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False

s = input().rstrip()
pattern = input().rstrip()
# pattern안에서 반복되는 pattern이 있는지 검사할 리스트.
pi = [0 for x in range(len(pattern))]

if KMP(s, pattern):
    print('1')
else:
    print('0')