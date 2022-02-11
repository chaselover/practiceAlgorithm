

def solution(id_list, report, k):
    user_list = {user: [0,[]] for user in id_list}
    mail_cnt = {user: 0 for user in id_list}
    # 각 유저 한번에 한명 신고 가능. 한 유저 여러번 신고 가능하나 명당 1번 카운트.
    for repo in report:
        a, b = repo.split()
        if a not in user_list[b][1]:
            user_list[b][1].append(a)
            user_list[b][0] += 1
    for user in user_list:
        if user_list[user][0] >= k:
            for send_mail in user_list[user][1]:
                mail_cnt[send_mail] += 1
    answer = []
    for mail in mail_cnt:
        answer.append(mail_cnt[mail])
    return answer
    # k번 신고되면 게시판 정지. 해당 유저 신고한 모든 유저에게 정지사실을 메일로 발송.
    # 정지 돼도 신고 가능.


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))