def solution(numbers):
    answer = []
    bin_numbers = []
    for number in numbers:
        bin_numbers.append(bin(number)[2:])
    
    def dfs(num, idx, level, start, end, key):
        if level == 0:
            return True
        if key and num[idx] == '1':
            return False
        if num[idx] == '0':
            key = 1
        if dfs(num, (idx + start) // 2, level - 1, start, idx, key) and dfs(num, (idx + end) // 2, level - 1, idx, end, key):
            return True
        return False
        
    for number in bin_numbers:
        k = len(number)
        cnt = 0
        while k:
            k //= 2
            cnt += 1
        number = '0' * (2**cnt - 1 - len(number)) + number
        # 모든 리프노드가 0이면 x
        # dfs 타다가 0나오면 쭉 타다가 1나오면 안됨. 0나오고 1나오면 안됨.
        if dfs(number, len(number) // 2, cnt, -1, len(number), 0):
            answer.append(1)
            continue
        answer.append(0)
        
    return answer

print(solution([15, 58, 63, 111, 95, 14, 42, 10, 104]))