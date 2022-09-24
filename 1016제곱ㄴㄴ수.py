min, max = map(int, input().split())

chk = [1] * (max - min + 1)
# 2부터 max의 제곱근 수까지만 체크하면 충분.
for n in range(2, int(max ** 0.5) + 1):
    square = n ** 2
    i = min // square
    # 제곱수의 배수가 min보다 크도록 나눈몫+1해줌.
    # 거기서부터 쭉 i증가시키며 돌고 n번째 수 다 끝나면 다음 n으로 넘어가며 check배열에 0으로 바꿔줌.
    if square * i < min:
        i += 1
    while square * i <= max:
        chk[square * i - min] = 0
        i += 1
print(sum(chk))


