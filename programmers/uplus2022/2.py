def solution(compressed):
    number = {str(i) for i in range(10)}
    alphas = {chr(i) for i in range(97, 123)}
    nums = []
    words = ['']
    tmp_n = []
    for char in compressed:
        if char in number:
            if not tmp_n:
                words.append('')
            tmp_n.append(char)
        elif char == '(':
            nums.append(int(''.join(tmp_n)))
            tmp_n = []
        elif char in alphas:
            words.append(words.pop() + char)
        else:
            tmp = ''
            for _ in range(len(words) - len(nums)):
                tmp += words.pop()
            words.append(tmp * nums.pop())
    return ''.join(words)
print(solution('xxx2(3(hi)co)'))