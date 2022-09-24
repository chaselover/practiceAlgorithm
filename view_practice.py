#검사해서 좌우 두칸에 나보다 작은 숫자만 있으면 됨.


def view():
    width = int(input())
    building = list(map(int,input().split()))
    cnt = 0
    for i in range(2, len(building)):
        if building[i]>building[i-1] and building[i]>building[i-2] and building[i]>building[i+1] and building[i]>building[i+2]:
            cnt += min(building[i]-building[i-1],building[i]-building[i-2],building[i]-building[i+1],building[i]-building[i+2])
    return cnt

for j in range(1,11):
    print("#{0} {1}".format(j, view()))