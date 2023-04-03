from collections import deque  # popleft와 같은 함수를 쓰기 위한 모듈

'''
n edge
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# n: 정점의 개수, edge: 간선의 개수
n, edge = map(int, input().split())

# 인접 리스트 : 정점 i -> 다른 정점에 대한 연결 정보
# 정점이 1부터 시작하니까 n+1로 만들어주기
graph = [[0] * (n+1) for _ in range(n+1)]

# 간선 정보 입력을 받고, 그것을 인접 리스트에 적용
arr = list(map(int, input().split()))
for i in range(0, len(arr), 2):
    # u = 정점 i <-> v = 정점 (i+1) 서로 연결
    u = arr[i]
    v = arr[i+1]
    graph[u].append(v)  # u -> v
    graph[v].append(u)  # v -> u

# 방문 정점을 체크하는 visited
visited = [False for _ in range(n+1)]

def bfs(v):  # 탐색 시작점 v
    # 큐 생성
    q = deque()
    # 시작점 v를 큐에 삽입
    q.append(v)  # 넣는건 오른쪽에서 넣으니까
    # 점 v를 방문한 것으로 표시
    visited[v] = True
    # while 큐가 비어있지 않은 경우일 동안
    while len(q) > 0:
        # t <- 큐의 첫번째 원소 반환
        t = q.popleft()  # 빼는건 왼쪽부터 빼야됨.
        print(t, end=', ')
        # For t와 연결된 모든 선에 대해
        #    u <- t의 이웃점
        for u in graph[t]:
            #  u가 방문되지 않은 곳이면,
            if visited[u] == False:
                # u를 큐에 넣고, 방문한 것으로 표시
                q.append(u)
                visited[u] = True

bfs(1)  # BFS 방식으로 1번 노드부터 순회해라!