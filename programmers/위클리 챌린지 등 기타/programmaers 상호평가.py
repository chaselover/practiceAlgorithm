def solution(scores):
    result  = ''
		
		# 각 학생에게 평가된 점수를 리스트 s로 변환
    for i in range(len(scores)):
        s = []
        for j in range(len(scores)):
            s.append(scores[j][i])
				# min, max에 해당하면서 유일값이면 해당 점수 제거
        if s[i] == min(s) and s.count(s[i]) == 1: del s[i]
        elif s[i] == max(s) and s.count(s[i]) == 1: del s[i]

        mean = sum(s) / len(s)
				
				# 학점 변환
        if mean >= 90: result += 'A'
        elif mean >= 80: result += 'B'
        elif mean >= 70: result += 'C'
        elif mean >= 50: result += 'D'
        else: result += 'F'
    return result


# .풀이 2
solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))


# 풀이3
def solution(scores) :

    avgs=[]

    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])


# 풀이 4
def solution(scores):
    answer = ''

    for i, score in enumerate(zip(*scores)):
        avg = (sum(score) - score[i]) / (len(score) - 1) if score[i] in (min(score), max(score)) and score.count(score[i]) == 1 else sum(score) / len(score)
        answer += "%s" % (
            "A" if 90 <= avg else
            "B" if 80 <= avg else
            "C" if 70 <= avg else
            "D" if 50 <= avg else
            "F"
        )

    return answer


