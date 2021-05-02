# 본 코드는 text안에 찾는 pattern 이 있으면 1 없으면 0 을 출력해주는 코드이다

# 보이어무어 알고리즘을 적용했다.

 

# 보이어무어 알고리즘이란 다음과 같다

# pattern의 오른쪽 끝 문자와 text의 현재 위치의 문자가 일치하는지 검사
# 끝이 일치하면 pattern과 text를 다 검사한다. 마지막까지 일치하지 않으면 패턴길이만큼 skip
# 끝이 일치하지않으면 text의 현재위치 문자가 skip배열에 있는지 확인. 있으면 인덱스만큼 skip, 없으면 패턴길이만큼 skip
# 텍스트 끝 도달할 때까지 반복

text = 'a pattern matching algorithm'
pattern = 'rithm'
s = pattern[::-1]
skip = list(range((len(pattern))))
 
i = len(pattern)-1
result = 0
 
while i < len(text):
    nxt = len(s)
    j = 0
    if s[j] == text[i]:
        while j < len(s):
            if s[j] != text[i-j]:
                break
            j += 1
        if j == len(s):
            result = 1
    else:
        while j < len(s):
            if s[j] == text[i]:
                nxt = min(j, nxt)
                break
            j += 1
    if result:
        break
    i += nxt
 
print(result)


# 고지식한 패턴검색 알고리즘 = Brute Force. 텍스트의 모든 위치에서 패턴비교 O(MN)

# KMP 알고리즘. 불일치 발생한 앞부분 대해 다시 비교하지 않고 매칭 수행 O(M+N)=O(N)
# next 배열을 생성해 불일치 발생하면 이동할 다음위치 저장.
# 패턴 왼쪽에서 오른쪽으로 비교

# 보이어 무어 알고리즘. 앞부분보다 끝부분가서 불일치 일어날 확률이 높다는 것 이용
# 일반적으로는 O(N) 보다 적은 수행시간. 최악일땐 O(MN)
# skip 배열 생성해서 일치하는 칸으로 몇칸 이동해야하는지 저장
# 패턴 오른쪽에서 왼쪽으로 비교.

# 그러면 3가지 패턴매칭 알고리즘을 비교해보자. M은 패턴의 길이, N은 텍스트의 길이
# Brute Force(=고지식한 패턴검색 알고리즘)
# 텍스트의 모든 위치에서 패턴 비교하고 한칸씩 이동한다.
# 시간복잡도 O(MN)
# KMP
# 불일치 발생한 앞부분에 대해 다시 비교하지 않고 매칭 수행
# next배열을 생성해 불일치 발생하면 이동할 다음 위치 저장
# 패턴의 왼쪽에서 오른쪽으로 비교
# 시간복잡도 O(M+N) = O(N)
# 보이어무어
# 앞부분보다 끝부분가서 불일치 일어날 확률이 높다는 것 이용
# skip 배열 생성해서 일치하는 칸으로 몇 칸 이동해야하는지 저장
# 패턴의 오른쪽에서 왼쪽으로 비교
# 상용화된 제품이나 서비스에 가장 많이 적용됨
# 시간복잡도 일반적으로 O(N) 이하. 최학일땐 O(MN) 