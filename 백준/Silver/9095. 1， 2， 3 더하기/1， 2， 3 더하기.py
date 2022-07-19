N = int(input())                                #케이스의 개수를 입력받음

def dp(x):                                      #문제풀이를 위한 재귀함수 정의
    if x == 1:                                  #예외상황 1, x=1일 경우 1 반환
        return 1
    elif x == 2:                                #예외상황 2, x=2일 경우 2 반환
        return 2
    elif x == 3:                                #예외상황 3, x=3일 경우 4 반환
        return 4
    else:
        return dp(x-1) + dp(x-2) + dp(x-3)      #나머지 점화식에 따라 1의 경우값, 2의 경우값, 3의 경우값을 재귀호출한다

for i in range(N):                              #케이스의 개수만큼 반복입력 받기
    num = int(input())                          #임의의 수 num 받음
    print(dp(num))                              #재귀함수 dp호출

    