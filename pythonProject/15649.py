n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:
        print(' ' . join(map(str, s)))  # int형으로 하면 오류, string형으로 넣어줘야함
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()  # 기점으로 열 원소로 들어감
            s.pop()


dfs()
