from sys import stdin
input = stdin.readline

def dfs(depth, string):
    global N, ret, charSet, cntMap

    if depth == N:
        # print(string)
        ret += 1
        return

    for char in charSet:
        idx = ord(char) - ord('a')
        # 알파뱃 카운트가 0이면 그 알파뱃으로 돌지 않는다. 
        if cntMap[idx] == 0:
            continue
        # 중요한게 string''면 -1인덱스 오류날텐데 string존재여부를 앞에 두어 없으면 앞에서 False나서 돌아가게 설계.! 기억할것.
        # 문자열이 존재하고 문자열 -1값이 알파뱃이랑 같으면 돌지 않는다.
        if string and string[-1] == char:
            continue
        # 문자열이 비었거나 알파뱃카운트가 있고 전이랑 지금알파뱃이 다를때.
        # 알파뱃 카운트 컨트롤, depth늘려주며 길이 체크, string에 문자추가.
        cntMap[idx] -= 1
        dfs(depth + 1, string + char)
        cntMap[idx] += 1


raw = input().strip()
cntMap = [0] * 26
N = len(raw)
ret = 0
charSet = set()

for char in raw:
    idx = ord(char) - ord('a')
    cntMap[idx] = cntMap[idx] + 1
    charSet.add(char)
# print(charSet, cntMap, cntSum)

dfs(0, '')
print(ret)