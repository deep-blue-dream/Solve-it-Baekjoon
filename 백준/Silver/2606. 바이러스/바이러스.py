# bfs 이용이 좋을 것 같은데, 가까운 것 부터 먼저 간다.
# 맵 그리기 먼저 해보자. 

from collections import deque

n = int(input())
conn_com = int(input())
graph = [[] for i in range(n+1)]           #빈 그래프 만든다.
visited = [0]*(n+1)
count = 0

for i in range(conn_com):
    a,b = map(int, input().split())        #컴퓨터 연결 그래프 디자인(양방향으로 연결)
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(graph, v):
    global count
    queue = deque([v])                     #BFS 풀이방식으로 queue 사용 
    
    while queue:                           #queue가 모두 비워질때(false)까지 반복한다.
        pop = queue.popleft()              #가장 먼저 기입된 요소를 pop하면서 방문표시를 한다.
        visited[pop] = 1
        
        for i in graph[pop]:               #pop된 요소가 있는 그래프 중에서 꺼냈을때
            if visited[i] == 0:            # 방문안한게 있다면
                visited[i] = 1             # 방문표시를 한 뒤
                queue.append(i)            # 방문표시가 된 컴퓨터의 리스트가 가지고 있는 요소를 큐에 넣는다
                count += 1                 # 카운트 1 올린다
    print(count)

bfs(graph,1)
