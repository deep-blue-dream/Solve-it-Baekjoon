#n,m 입력받기
n,m = map(int,input().split())

#빈 그래프 만들기
graph = []

#그래프 그리기
for i in range(n):
    graph.append(list(map(int,input())))
    
#출력하고자 하는 값 area(정사각형 면적)를 1로 초기화
area = 1

#그래프에서 순회하면서 정사각형 찾기 로직 구현
for i in range(n):
    for j in range(m):
        #정사각형 판단하기 k만큼 더했을때 각 가로, 세로가 같은 값인지 판단 1부터 시작
        k = 1
        
        #k값(정사각형 탐색범위)이 행과 열을 벗어나면 반복 종료
        while 1:
            if (i+k) == n or (j+k) ==m:
                break
            # 시작점(target)과 각 모서리 점이 같은 값인지 확인하기 and조건 중첩
            if graph[i][j] == graph[i+k][j] and graph[i][j] == graph[i][j+k] and graph[i][j] == graph[i+k][j+k]:
                area = max(area, (k+1)**2)
            
            #각 포인트 탐색 조건 종료시 k 값 증가
            k += 1
#최종 결과 출력
print(area)          
       
                
                