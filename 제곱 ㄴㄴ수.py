# 에라토스테네스의 체 활용
# 기존은 isPrime을 통해 소수 수집 후 소수의 배수들을 걸러주는 방법.
# 이번엔 n^2수들의 배수를 배제하는 방법.
# 1. 검사할 숫자들을 배제하기위한 False배열(최대검사수만큼)
# 2. 제곱들이 저장되는 배열(범위 내 제곱값까지.)
# 3. 제곱의 배수 갯수 저장할 cnt
# 4. 제곱수로 나누어 떻어지는 값들을 최대, 최소값 사이로 민다.(j를 늘려가며)
# 체를통해 중복체크하는 것만 없애면 시간복잡도는 n에 수렴한다.

min_num,max_num = map(int,input())
# 1
eratos_filter = [False for _ in range(max_num-min_num+1)]
# 3
cnt = max_num-min_num+1
i = 2
while i**2 <= max_num:
    # i는2부터 i제곱의 으로 안나눠 떨어지면 s+1부터 min이랑 max사이로 들어옴.
    s = min_num//(i**2)
    if min_num % (i**2) != 0:
        s +=1
    
    while s*(i**2) <= max_num:
        if not eratos_filter[s*(i**2)-min_num]:
            eratos_filter[s*(i**2)-min_num] = True
            # 카운트는 최대 값부터 배수하나 찾을때마다 -1씩해줌.
            cnt -= 1
        s+=1
    i += 1

print(cnt)