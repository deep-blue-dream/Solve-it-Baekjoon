H, M = map(int, input().split())     # 두 정수를 입력 받는다.

def alarm(x,y):                      # 함수 alarm을 정의한다.인자값 2개(시간,분)을 넣을 예정
    y -= 45                          # 우선 분에 45를 뺀다. (여기선 시간을 빼지 않았다)
    
    if y < 0 :                       # 만약 분이 0보다 작다면
        y = y + 60                   # 분에 60을 더한다
        x -= 1                       # 시간에 1을 뺀다
        
        if x < 0 :                   # 만약 뺀 시간이 0보다 작다면
            x += 24                  # 시간에 24를 더한다
    
    return print(x,y)                # 최종적으로 시간과 분을 출력한값을 반환한다.


alarm(H,M)                           #선언된 함수를 불러온다.