import sys
input = sys.stdin.readline

#암호와 비교값k 입력받기 
key,k = map(int,input().split())

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

#k 이하의 소수 목록 산출
solv_list = prime_list(k)


key_list=[]

#인증과정
for i in solv_list:
    if key % i == 0:
        key_list.append(i)

#k 아래 인증과정에 해당하는 소수 쌍이 없다면 GOOD 출력, 있다면 작은소수 출력
if len(key_list) == 0:
    print("GOOD")
else:
    print("BAD", key_list[0], sep=' ')
