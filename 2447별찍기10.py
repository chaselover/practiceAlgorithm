# 분할 정복 알고리즘 / 분할, 정복, 합치기.

# 정복
# star 배열을 통해 새 matrix를 생성해 반환하는게 목적.
# 반복문에서 3*len(star)로 별이 그려지는 모든 배열을 검사하며 len(star)
# 즉 최초 n의 크기에 따라 빈칸 " "을 추가적으로 삽입하는 방식을 차용한다.
# (n=9일때 3으로 나눠 몫이 1인 index = 1 요소의 가운데 )
def conquer(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

# default로 n=3일때 배열과 k값을 미리 줌.
star = ["***","* *","***"]
n = int(input())
k = 0

# 분할(3의k승형으로 분할. 최종적으로 n=3인 모형에 k값만 가지고 간다.
while n != 3:
    n = int(n / 3)
    k += 1

# 조합
# n=3일때 conquer의 결과를 확장시켜 n=9를 그린다. k승만큼 반복한다.
for i in range(k):
    star = conquer(star)
for i in star:
    print(i)