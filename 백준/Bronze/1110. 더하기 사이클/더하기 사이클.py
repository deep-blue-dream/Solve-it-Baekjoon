N = int(input())               #정수값 입력받기
num = N                        #가공 전 할당
count = 0                      #횟수 초기화

while True:                    #무한반복
    a = num //10               #N의 10의 자리
    b = num % 10               #N의 1의 자리
    c = (a+b)%10               #a+b의 1의 자리
    num = b*10 + c             #num 변수에 재할당
    
    count += 1                 # 횟수 증가
    if num == N:               # 종료조건
        break                  

print(count)                   # 결과 출력

