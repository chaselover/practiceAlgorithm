# 브루트 or 투포인터

from collections import deque

def check_issue(counter,n,k):
    for char in counter:
        if counter[char] >= k:
            n_cnt[char][0] += 1
            n_cnt[char][1].append(counter[char]) 
            if n_cnt[char][0] >= n:
                if sum(n_cnt[char][1]) >= 2*n*k:
                    issue_word[char] += 1
                n_cnt[char][0] -= 1
                n_cnt[char][1].popleft()
        else:
            n_cnt[char][0] = 0
            n_cnt[char][1] = deque()


def solution(research, n, k):
    global n_cnt, issue_word
    n_cnt = {chr(i): [0,deque()] for i in range(97,97+26)}
    issue_word = {chr(i): 0 for i in range(97,97+26)}
    for search in research:
        counter = {chr(i): 0 for i in range(97,97+26)}
        for word in search:
            counter[word] += 1
        check_issue(counter,n,k)
    max_cnt = 0
    hot_issue_word = 0
    for word in issue_word:
        if max_cnt < issue_word[word]:
            hot_issue_word = word
            max_cnt = issue_word[word]
    if not hot_issue_word:
        hot_issue_word = 'None'
    return hot_issue_word



print(solution(["abaaaa","aaa","abaaaaaa","fzfffffffa"],2,2))