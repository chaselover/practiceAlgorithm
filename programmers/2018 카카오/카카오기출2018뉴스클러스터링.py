from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_elements_set = []
    str2_elements_set = []
    # 두글자씩 끊어 원소집합으로 만듦(둘다 알파뱃일 경우만.)
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_elements_set.append(str1[i] + str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            str2_elements_set.append(str2[j] + str2[j+1])
    # 각 원소 집합에 대해 카운터 객체 생성.
    Counter1 = Counter(str1_elements_set)
    Counter2 = Counter(str2_elements_set)
    # 교집합(양쪽 다 원소의 갯수가 같은만큼만 원소추출)
    inter_strs = list((Counter1 & Counter2).elements())
    # 합집합(모든 원소)
    union_strs = list((Counter1 | Counter2).elements())
    # 유사도는 교집합 크기/합집합 크기 * 65536 의 소숫점 버림.
    # ex
    # Counter({'aa': 2}) Counter({'aa': 3})
    # ['aa', 'aa'] ['aa', 'aa', 'aa']
    # 43690
    if len(union_strs) == 0 and len(inter_strs) == 0:
        return 65536
    else:
        return int(len(inter_strs) / len(union_strs) * 65536)

print(solution('aa1+aa2','AAAA12'))