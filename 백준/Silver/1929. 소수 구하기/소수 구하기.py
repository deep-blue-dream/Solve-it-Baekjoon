def isPrime(num):        #소수 판별함수
    if num==1:           # 1은 false 처리
        return False
    else:      
        for i in range(2, int(num**0.5)+1):        #입력값의 제곱근까지만 순환
            if num%i == 0:                         #i 값으로 나누어 떨어지면 소수가 아님
                return False
        return True                               #if가 아니면 참임

M, N = map(int, input().split())                  #값 입력받기

for i in range(M, N+1):                           #시작부터 끝까지 조회
    if isPrime(i):                                #함수 조회
        print(i)                                  #해당 순서가 맞으면 출력
