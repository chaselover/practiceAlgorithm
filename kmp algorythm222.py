def kmp_match(txt: str, pat: str) -> int:
    # 스킵테이블 만들기
    def make_skip_table(skip: list):
        pt = 1  # txt를 따라가는 인덱스
        pp = 0  # pat를 따라가는 인덱스
        while pt < len(pat):
            if pat[pt] == pat[pp]:
                pt += 1
                pp += 1
                skip[pt] = pp
            elif pp == 0:
                pt += 1
                skip[pt] = pp
            else:
                pp = skip[pp]

    # 부분 문자열 찾기 (이 문제에서는 있는지 없는지만 찾으면 된다.)
    def find_match_idx(txt: str, pat: str) -> int:
        pt = 0
        pp = 0
        while pt < len(txt) and pp < len(pat):
            if txt[pt] == pat[pp]:
                pt += 1
                pp += 1
            elif pp == 0:  # 더 이상 앞으로 돌아갈 수 없는 경우
                pt += 1
            else:
                pp = skip[pp]
        if pp == len(pat):
            return 1
        else:
            return 0

    skip = [0] * (len(pat) + 1)
    make_skip_table(skip)
    answer = find_match_idx(txt, pat)
    print(answer)


if __name__ == '__main__':
    S = input()
    P = input()
    kmp_match(S, P)