import sys
sys.stdin = open('input.txt')


def find_palindrome(sentences):
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(100-k+1):
                if sentences[i][j] == sentences[i][j+k-1]:
                    left = j
                    right = j+k-1
                    while sentences[i][left] == sentences[i][right] and left <= right:
                        left += 1
                        right -= 1
                    if left < right:
                        continue
                    else:
                        max_length = k
                        return max_length


for _ in range(10):
    test = int(input())
    palindrome = [list(input().rstrip()) for _ in range(100)]
    result1 = find_palindrome(palindrome)
    reverse_palindrome = list(zip(*palindrome))
    result2 = find_palindrome(reverse_palindrome)
    print(f"#{test} {max(result1,result2)}")
