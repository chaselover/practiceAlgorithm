def mobius(n):
    m = [0] + [1] * n
    for i in range(2, n + 1):
        if m[i] == 0: continue
        for j in range(2 * i, n + 1, i):
            m[j] -= m[i]
    return m


def count(m, k):
	x = 0
	for i in range(2, int(k ** .5) + 1):
		if m[i] == 0: continue
		else: x += m[i] * (k // (i * i))
	return x


k = int(input())
left = int(k * 2.5)
right = int(k * 4 if k < 10 else k * 3 if k < 104 else k * 2.6 if k < 10000 else k * 2.551)
m = mobius(int(right ** .5))

while left <= right:
	mid = (left + right) // 2
	non = count(m, mid)
	if non < k: left = mid + 1
	else: right = mid - 1

print(left)
