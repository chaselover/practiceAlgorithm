class Solution:
    def diffWaysToCompute(self, input: str):
        def operation(le, ri, oper):
            sm = 0
            result = []
            for l in le:
                for r in ri:
                    if oper == "+":
                        sm = l + r
                    elif oper == "-":
                        sm = l - r
                    elif oper == "*":
                        sm = l * r
                    result.append(sm)
            return result
        results = []
        
        # 연산자없이 오직 숫자만을 가질 때 리스트 형태로 바로 반환.
        if input.isdigit():
            return [int(input)]
        
        # 연산이 수행되는 순서에 따라 값이 달라지므로 모든 경우를 구하기 위해 반복이 필요하다.
        for i in range(len(input)):
            if input[i] in '+-*':
                # 현재 연산자 기준으로 분할
                left = self.diffWaysToCompute(input[:i])
                right= self.diffWaysToCompute(input[i + 1:])
                
                # 양쪽 결과를 병합해서 나온 값들을 넣어줌
                # 여러 값이 리스트로 나오는 것은 순서마다 나올 수 있는 값이 다르기 때문!
                results.extend(operation(left, right, input[i]))
        return results