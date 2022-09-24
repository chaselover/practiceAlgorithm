#coding: utf-8

#성적 총점 평점.

scores = []

count = int(input("총 학생 수를 입력하세요:"))

for i in range(1, count+1):
    score = []
    kor = int(input("학생{0}의 국어점수를 입력하세요:".format(i)))
    score.append(kor)
    mat = int(input("학생{0}의 수학점수를 입력하세요:".format(i)))
    score.append(mat)
    eng = int(input("학생{0}의 영어점수를 입력하세요:".format(i)))
    score.append(eng)
    scores.append(score)

for score in scores:
    total = 0
    for s in score:
        total += s
    print("총점: {0}, 평균:{1:0.2F}".format(total, total/len(score)))
