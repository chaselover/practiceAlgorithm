import sys
 
 
def next_permutation(list_a):
    k = -1
    m = -1
 
    # 증가하는 마지막 부분을 가리키는 index k 찾기
    for i in range(len(list_a)-1):
        if list_a[i] < list_a[i+1]:
            k = i
 
    # 전체 내림차순일 경우, 반환
    if k == -1:
        return [-1]
 
    # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
    for i in range(k, len(list_a)):
        if list_a[k] < list_a[i]:
            m = i
 
    # k와 m의 값 바꾸기
    list_a[k], list_a[m] = list_a[m], list_a[k]
 
    # k index 이후 오름차순 정렬
    list_a = list_a[:k+1] + sorted(list_a[k+1:])
    return list_a
 
 
# 주어진 값 입력 & 정렬
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
 
ans = 0
# 첫 순열 내 값 차이를 더해(s), ans 보다 크면 ans를 update
s = 0
for j in range(len(a) - 1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s
 
arr = a
 
while True:
    arr = next_permutation(arr)
    if arr == [-1]:
        break
    s = 0
 
    # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
    for j in range(len(arr) - 1):
        s += abs(arr[j] - arr[j+1])
    if s > ans:
        ans = s
 
print(ans)