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



# dfs 순회 (재귀호출)
def dfs(v):  # v: 정점
    # 현재 방문한 정점은 v임
    visited[v] = True  # 방문 체크
    print(v, end=', ')  # 해당되는 정점 확인용

    # 현재 v 정점에 대해서 인접한 (방문하지 않은) 노드를 방문
    for u in graph[v]:
        if visited[u] == False:
            dfs(u)  # 방문 진행

dfs(1)