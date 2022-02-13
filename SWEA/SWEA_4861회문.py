import sys
input = sys.stdin.readline

def find_palindrome(N,M,sentences):
    for i in range(N):
        for j in range(N-M+1):
            if sentences[i][j] == sentences[i][j+M-1]:
                left = j
                right = j+M-1
                while sentences[i][left] == sentences[i][right] and left <= right:
                    left += 1
                    right -= 1
                if left < right:
                    continue
                else:
                    return sentences[i][j:j+M]

for test in range(1,int(input())+1):
    N, M = map(int,input().split())
    palindrome = list(list(input().rstrip()) for _ in range(N))
    result1 = find_palindrome(N,M,palindrome)
    if result1:
        print(f"#{test} {''.join(result1)}")
    else:
        reverse_palindrome = list(zip(*palindrome))
        result2 = find_palindrome(N,M,reverse_palindrome)
        print(f"#{test} {''.join(result2)}")
