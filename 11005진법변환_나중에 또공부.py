system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #10진법이면 9 까지, 36진법이면 Z까지 표현된다
N, B = map(int, input().split())
answer = ''

while N != 0:
    # N을 B로 나눈 나머지를 마지막칸에 채움(1의자리)(36진법이면 나머지 = 36진법중 2번째 숫자)
    answer += str(system[N % B]) #위치로 진법 변환
    # N을 B로 나눈 몫이 N이 된다.
    N //= B
    
    
print(answer[::-1])