
arr = list(map(int, input().split()))
pivot = [i for i in range(1, 9)]
if arr == pivot:
    print('ascending')
elif arr == pivot[::-1]:
    print('descending')
else:
    print('mixed')