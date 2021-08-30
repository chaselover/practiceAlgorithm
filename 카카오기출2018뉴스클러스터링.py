from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    # 두글자씩 끊어 원소집합으로 만듦(둘다 알파뱃일 경우만.)
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
    # 각 원소 집합에 대해 카운터 객체 생성.
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    # 교집합(양쪽 다 원소의 갯수가 같은만큼만 원소추출)
    inter = list((Counter1 & Counter2).elements())
    # 합집합(모든 원소)
    union = list((Counter1 | Counter2).elements())
    # 유사도는 교집합 크기/합집합 크기 * 65536 의 소숫점 버림.
    # ex
    # Counter({'aa': 2}) Counter({'aa': 3})
    # ['aa', 'aa'] ['aa', 'aa', 'aa']
    # 43690
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

print(solution('aa1+aa2','AAAA12'))