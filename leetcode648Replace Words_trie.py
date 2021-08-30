class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 트라이 자료구조 만들기
        root = {}
        for dic in dictionary:
            t = root
            for c in dic:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['*'] = True
 
        answer = []
        for word in sentence.split():
            t = root
            res = ''
 
            if len(word) == 1:
                if word in t:
                    answer.append(word)
                    continue 
 
            flag = 0
            for c in word:
                if '*' in t:
                    answer.append(res)
                    flag = 1
                    break
 
                if c not in t:
                    answer.append(word)
                    flag = 1
                    break
 
                t = t[c]
                res += c
 
            if flag == 0:
                answer.append(res)
 
        return " ".join(answer)