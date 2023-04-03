p = []
# 유니온-파인드 알고리즘
def make_set():
    global p
    p = [i for i in range(n+1)]  # [0(x 안 씀), 1, 2, 3, 4, 5, 6, 7] 각각 자기 자신을 대표로 갖는다

# 대표자를 찾는 (재귀)
# 이전 대표자를 현재 대표자로 정정하는 기능을 포함
# find 함수
def find_set(x):
    # 기저조건 (부모 노드로 자기자신을 갖는다면 해당 노드를 반환)
    if x == p[x]:
        return x

    # 재귀적으로 대표자에 대해 경로 압축이 진행 -> 현재 대표자로 정정
    p[x] = find_set(p[x])
    return p[x]

# 하나의 집합으로 합치는 union 함수
def union_set(x, y):  # x, y 를 받았을 때
    x = find_set(x)  # find 함수로 대표자 받아오기
    y = find_set(y)
    p[y] = x  # x 를 대표자로 선출
    return x

    # *예를 들어서 제약 조건이
    # (더 낮은 숫자의 노드를 대표자로 뽑아라!)
    # if x < y:
    #     p[y] = x
    #     return x
    # else:  # y < x
    #     p[x] = y
    #     return y



t = int(input())
for tc in range(1, t + 1):
    # n: 노드의 개수, m: 간선의 개수
    n, m = map(int, input().split())

    # 유니온-파인드 과정의 초기화 (make-set)
    make_set()

    # 간선의 개수만큼 노드 u <-> v에 대한 연결 정보
    for _ in range(m):
        # 노드 u <-> v 가 연결이 되어있음 (union-set)
        u, v = map(int, input().split())
        union_set(u, v)

    # 모든 노드를 순회하면서 어떤 집합이 있는지 확인
    # -> 대표자가 몇 명인지 확인
    reps = set()  # 대표자들
    for node in range(1, n+1):
        reps.add(find_set(node))  # 대표자를 set 자료형에 추가

    print(f'#{tc} {len(reps)}')

