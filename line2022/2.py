from typing import List

def solution(k: int, dic: List[str], chat: str):
    answer = []
    bad_words = set()
    # 미리 k개 만큼 .으로 변환시킨 단어를 저장
    for word in dic:
        tmp = []
        tmp.append(word)
            # 1개 ~ max개까지
        for dot_cnt in range(len(word)//k):
            for resource in tmp:
                 # dot을 넣을 위치
                for idx in range(len(resource)):
                        # dot의 size
                    for dot_size in range(1, k + 1):
                        if not '.' in resource[idx: idx + dot_size]:
                            tmp.append(resource[:idx] + "." + resource[dot_size + idx:])
                        
        for each_word in tmp:
            bad_words.add(each_word)
    for word in chat.split():
        if word in bad_words:
            answer.append('#' * len(word))
        else:
            answer.append(word)
    answer = ' '.join(answer)
    return answer




print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))