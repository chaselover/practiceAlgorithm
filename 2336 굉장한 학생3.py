import sys


def update(idx, val):
    while idx <= n:
        tree[idx] = min(tree[idx], val)
        idx += (idx & -idx)


def query(end):
    ret = float('inf')

    while end > 0:
        ret = min(ret, tree[end])
        end -= (end & -end)

    return ret

n = int(sys.stdin.readline())
student = [[] for _ in range(n + 1)]
tree = [float('inf')] * (n + 1)
student[0] = [0, 0, 0]

for _ in range(3):
    temp = list(map(int, sys.stdin.readline().split()))

    for i in range(1, n + 1):
        num = temp[i - 1]
        student[num].append(i)

student.sort(key=lambda x:x[0])

ans = 0
for i in range(1, n + 1):
    sec_exam, thi_exam = student[i][1], student[i][2]
    former_rank = query(sec_exam)

    if former_rank > thi_exam:
        ans += 1

    update(sec_exam, thi_exam)

print(ans)