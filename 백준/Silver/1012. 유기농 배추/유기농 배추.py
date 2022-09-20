#테스트 케이스 입력받음
T = int(input())

#델타값 선정
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#BFS 메서드 작성
def BFS(x,y):
    #queue는 1이 있는 곳을 좌표값으로 받을 예정(각 지점을 스코프로 지나가므로 좌표로 탐색)
    queue = [(x,y)]
    
    #방문 지점을 체크 처리하기
    graph[x][y] = 0
    
    #queue가 비워질 때까지 반복
    while queue:
       
        #queue의 첫번째 좌표 값을 x,y에 할당
        x,y = queue.pop(0)
    
        #델타탐색(좌,우,하,상)4번
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            #만약 그래프의 델타탐색 방향이 범위(N,M)를 넘어가면 pass
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            
            #델타탐색 좌표가 1이라면 quque에 좌표값(x,y)로 삽입(연결된 부분 모두 0으로 처리해야 하므로)
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                #해당 지점은 0으로 변경
                graph[nx][ny] = 0
            
            
#테스트 케이스 수 만큼 그래프 작성 및 BFS 호출
for i in range(T):
    
    #결과값 선언(애벌레 마릿수)
    count = 0
    
    #그래프의 크기와 배추의 갯수 입력받음
    N,M,num = map(int,input().split())
    
    #기본 그래프 생성(리스트 표현식 미스났었음)
    graph = [[0]*M for _ in range(N)]
    
    #배추심기(x,y)좌표 값으로 받아서 심음
    for i in range(num):
        x,y = map(int, input().split())
        graph[x][y] = 1
        
    #그래프 탐색 시작(0,0)~(N,M)까지
    for a in range(N):
        for b in range(M):
            
            #탐색지점이 1일 경우 BFS 시작, 결과값 변경
            if graph[a][b] == 1:
                BFS(a,b)
                count += 1
    print(count)