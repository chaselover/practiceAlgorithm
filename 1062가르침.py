from itertools import combinations
n, k = map(int, input().split())
# 글자가 5개 미만이면 antic도 못배우니까 어떤 글자도 배울 수 없다.
if k < 5:
    print(0)
else:
    # 일단 5개배우고 시작.
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    # a~z중 antic뺀 나머지 chr들.을  index와 짝지어 딕셔너리 형태로 저장.(a:0,b:1....)숫자가 임의로 설정되어있음.
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    print(alpha)
    cnt = 0
    # n번의 글자입력
    for _ in range(n):
        tmp = 0
        # 배운 글자를 뺀 나머지 글자c들에 대해 순회하며 비트마스킹 한 숫자를(필요한 숫자에 마스킹) tmp에 표기해 input_chars에 저장..(나온 글자들에 불을 켜.)
        for c in set(input())-nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
        # antic을 뺀 나머지 21개글자를 나타내는 숫자들(2의 n승이 비트마스킹에서 각자리 1을 나타내기 때문)(그 숫자들중 k개를 뽑는 조합을 다 순회.)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        # 조합의 sum은 input_chars에 들어있는 비트마스킹된 숫자들과 비교할 test에 저장.
        test = sum(comb)

# input_chars에 넣어둔 필요한 알파뱃 조합들과 test로 생성한 남은 알파뱃중 만들수 있는 모든 조합과 비교해 일치하면 cnt하나 상승.
# test 문자(합이 문자)와 input_char에서 그 test숫자로 만들수있는 단어의 수를 세어ct에 저장하고 cnt에 최댓값 저장.
# (각 문자 셋을 조합으로 만들어 비교 후 최대 몇개 만족하나 저장.)
        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)