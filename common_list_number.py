#coding: utf-8

#학생별, 과목별 총점 및 평균 구하기

scores = []

count = int(input("총 학생의 수를 입력하세요:"))

for i in range(1, count+1):
    score = {}
    score["name"] = input("학생의 이름을 입력하세요:")
    score["kor"] = int(input("{0} 학생의 국어 점수플 입력하세요:".format(score["name"])))
    score["mat"] = int(input("{0} 학생의 수학 점수플 입력하세요:".format(score["name"])))
    score["eng"] = int(input("{0} 학생의 수학 점수플 입력하세요:".format(score["name"])))
    scores.append(score)

for score in scores:
    total = 0
    for key in score:
        if key != "name":
            total += score[key]
    print("{0}학생 => 총점:{1}, 평균 : {2:0.2F}".format(score["name"],total,total/3))