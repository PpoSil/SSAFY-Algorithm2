'''
money(int) 32888
-> list(str) ['3', '2', '8', '8', '8']
-> or list(float) [3, 2, 8, 8, 8]
'''


def dfs(money, count):
    global existed
    '''
    :param money: 상금(금액)- 문자열 형태임. 리스트로 바꾸자!
    :param count: 교환 횟수
    '''

    # 기저조건(count 값이 모두 소진되었을 때)
    if count == 0:
        existed[count].add(int(''.join(money)))
        return

    # 가지치기
    if int(''.join(money)) in existed[count]:
        return

    existed[count].add(int(''.join(money)))

    # 메인로직 (재귀함수)
    for i in range(len(money)):
        for j in range(i + 1, len(money)):
            money[i], money[j] = money[j], money[i]  # 수정
            dfs(money, count - 1)
            money[i], money[j] = money[j], money[i]  # 복구


t = int(input())
for tc in range(1, t + 1):
    # money: 상금, count: 교환 횟수
    money, count = map(int, input().split())


    existed = [set() for _ in range(count+1)]
    dfs(list(str(money)), count)

    print(f'#{tc} {max(existed[0])}')

